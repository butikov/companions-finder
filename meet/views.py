from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MeetSerializer
from .models import Meet


class MeetViewSet(viewsets.ModelViewSet):
    serializer_class = MeetSerializer
    queryset = Meet.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


