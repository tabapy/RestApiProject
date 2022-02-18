from django.contrib.auth import authenticate, get_user_model
from rest_framework import serializers
from account.models import MyUser

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_confirm')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirm = validated_data.get('password_confirm')
        if password != password_confirm:
            raise serializers.ValidationError('passwords do not match')
        return validated_data

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(email=email, password=password)
        user.create_activation_code()
        user.send_activation_code()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                message = 'Unable to log in with provided credentials'
                raise serializers.ValidationError(message, code='authorization')
        else:
            message = "Must include 'email' and 'password'."
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs


class ChangePasswordSerializer(serializers.Serializer):
    model = MyUser
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, old_pass):
        request = self.context.get('request')
        user = request.user

        if not user.check_password(old_pass):
            raise serializers.ValidationError('Вы ввели неправильный старый пароль')

        return old_pass

    def validate(self, attrs):
        old_pass = attrs.get('old_password')
        new_pass1 = attrs.get('new_password')
        new_pass2 = attrs.get('new_password_confirm')

        if new_pass1 != new_pass2:
            raise serializers.ValidationError('Новые пароли не совпадают')

        if old_pass == new_pass1:
            raise serializers.ValidationError('Новый и старый пароль не могут быть одинаковыми')
        return attrs

    def set_new_password(self):
        new_pass = self.validated_data.get('new_pass')
        user = self.context.get('request').user
        user.set_password(new_pass)
        user.save()