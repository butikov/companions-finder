from rest_framework import serializers
from .models import DefaultUser


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DefaultUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'subscriptions', 'password',)
        read_only_fields = ('id', 'subscriptions',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = DefaultUser(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
