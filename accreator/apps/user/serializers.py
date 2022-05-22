from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.utils import PasswordValidator


class BaseUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'email',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login'
        )
        read_only_fields = (
            'id',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login'
        )


class UserCreateUpdateSerializer(BaseUserSerializer):
    password = serializers.CharField(min_length=8, max_length=32, write_only=True)
    password_confirm = serializers.CharField(min_length=8, max_length=32, write_only=True)

    class Meta(BaseUserSerializer.Meta):
        fields = BaseUserSerializer.Meta.fields + (
            'password',
            'password_confirm'
        )

    def validate_password(self, password):
        if PasswordValidator(password).is_valid():
            return password
        raise ValidationError(
            'Password must contain: at least one digit, upper, lower and special characters without spaces'
        )

    def _validate_passwords_equal(self, password, password_confirm):
        return password == password_confirm

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirm = attrs.get('password_confirm')

        if not self._validate_passwords_equal(password, password_confirm):
            raise ValidationError('Passwords don\'t match')

        return attrs


class UserSerializer(BaseUserSerializer):
    pass
