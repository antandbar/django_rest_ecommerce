from rest_framework import serializers
from apps.users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

    def to_representation(self, instance):
        
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
        """
        return {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'clave': instance.password
        }
        """

"""
class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self, value):
        if 'developer' in value:
            raise serializers.ValidationError('Error, No puede existir un usuario en ese nombre')
        
        return value

    def validate_email(self, value):
        # Custom validation
        if value == '':
            raise serializers.ValidationError('Tiene que indicar un correo')

        if self.validate_name(self.context['name']) in value:
            raise serializers.ValidationError('El mail no puede contener el nombre')
        

        return value

    def validate(self, data):
        if data['name'] in data['email']:
            raise serializers.ValidationError('El email no puede contener el nombre')
        
        return data
    
    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
"""