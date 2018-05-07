from .models import Comment
from rest_framework import serializers
from meet.serializers import MeetSerializer


class CommentSerializer(serializers.ModelSerializer):

    content = MeetSerializer

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'content', 'created',)
        read_only_fields = ('id', 'author', 'content', 'created',)
