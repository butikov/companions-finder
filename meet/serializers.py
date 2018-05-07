from rest_framework import serializers
from .models import Meet
from user.serializers import UserSerializer


class MeetSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Meet
        fields = ('id', 'title', 'text', 'author', 'meet_time', 'participants', 'max_participants', 'created',
                  'coordinates', 'categories', 'like_count',)
        read_only_fields = ('id', 'author', 'participants', 'created', 'like_count',)
