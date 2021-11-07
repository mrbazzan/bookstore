
from rest_framework import serializers
from account.models import User


class UserSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        label='Password confirmation',
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'email', 'date_of_birth', 'name', 'is_kid', 'is_admin', 'profile', 'age', 'password', 'confirm_password']
        extra_kwargs = {
            "password": {"write_only": True},
        }

    def save(self):
        user = User(
            name=self.validated_data['name'],
            profile=self.validated_data['profile'],
            email=self.validated_data['email'],
            age=self.validated_data['age'],
            date_of_birth=self.validated_data['date_of_birth']
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError({"Password": "Password must match."})

        user.set_password(password)
        user.save()
        return user
