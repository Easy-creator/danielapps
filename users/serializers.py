from rest_framework import serializers
from users.models import NewUser

class RegisterationPoint(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)

    class Meta:
        model = NewUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password',)

    def create(self, validated_data):
        return NewUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120, min_length=6, write_only=True)

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password', 'token')
        read_only_fields = ['token']
