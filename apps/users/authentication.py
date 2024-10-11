from datetime import timedelta

from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ExpiringTokenAuthentication(TokenAuthentication):

    def expires_in(self,token):
        time_elapse = timezone.now() - token.created
        lef_time = timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS) - time_elapse
        return lef_time

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds = 0)

    def token_expired_handler(self, token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            user = token.user
            token.delete()
            token = self.get_model().objects.create(user = user)
        return token

    def authenticate_credentials(self, key):
        user = None
        try:
            # Devuelve el token de la librería
            token = self.get_model().objects.select_related('user').get(key = key)
            token = self.token_expired_handler(token)
            user = token.user
        except self.get_model().DoesNotExist:
            pass
        """
        if token is not None:
            if not token.user.is_active:
                message = 'Usuario no activo o eliminado'
                #raise AuthenticationFailed('Usuario no activo o eliminado')
        
            is_expired = self.token_expired_handler(token)
            if is_expired:
                message = 'Su token ha expirado'
                #raise AuthenticationFailed('Su token ha expirado')
        """
        
        return user
        
