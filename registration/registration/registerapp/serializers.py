from rest_framework import serializers
from .models import RegisterUser
from django.contrib.auth import password_validation


class RegisterSerializer(serializers.ModelSerializer):
    """
        Serializer for the register fields
    """
    password = serializers.CharField(style={
                                    'input_type': 'password'},
                                    write_only=True)
    confirm_password = serializers.CharField(style={
                                    'input_type': 'password'},
                                    write_only=True)

    class Meta:
        model = RegisterUser
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'confirm_password'

        ]

    def validate(self, data):
        """
        Validating the password
        """
        pass1 = data.get('password')
        pass2 = data.pop('confirm_password')
        if pass1 != pass2:
            raise serializers.ValidationError("password does not match")
        password_validation.validate_password(pass1)
        return data


class SerializerList(serializers.ModelSerializer):
    class Meta:
        model= RegisterUser
        fields=['id','email','first_name','last_name',]
