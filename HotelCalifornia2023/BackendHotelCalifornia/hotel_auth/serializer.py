from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import make_password
from GestionUsuarios.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    imagen=serializers.CharField(required=False),
    nombre=serializers.CharField(required = True),
    apellido=serializers.CharField(required = True),
    usuario=serializers.EmailField(required = True),
    password=serializers.CharField(required = True),
    fechaDeNacimiento=serializers.DateField(required = True),
    telefono=serializers.CharField(required = True)
    ciudad=serializers.CharField(required = True)
    class Meta:
        model = get_user_model()
        fields = ("imagen", "nombre", "apellido", "usuario", "password", "fechaDeNacimiento", "telefono", "ciudad")
    def validate_password(self, value):
        return make_password(value)
    
class LoginSerializer(serializers.Serializer):
    usuario = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})

    def validate(self, attrs):
        usuario = attrs.get('usuario')
        password = attrs.get('password')

        if usuario and password:
            user = authenticate(username=usuario, password=password)

            if not user:
                raise serializers.ValidationError('Invalid credentials')

            if not user.is_active:
                raise serializers.ValidationError('User account is disabled')

        else:
            raise serializers.ValidationError('Must include "usuario" and "password"')

        attrs['user'] = user
        return attrs