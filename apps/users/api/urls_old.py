from django.urls import path
#from apps.users.api.api import UserApiView
from apps.users.api.api import user_api_view, user_detail_api_view

""" Se crea ruta sin decorador
urlpatterns = [
    path('usuario/', UserApiView.as_view(), name = 'usuario_api')
]"""

urlpatterns = [
    path('usuario/', user_api_view, name = 'usuario_api'),
    path('usuario/<int:pk>/', user_detail_api_view, name = 'usuario_detail_api_view')
]
