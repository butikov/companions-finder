from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from user.serializers import UserSerializer
from core.permissions import IsAdminOrIsCurrentUserOrReadOnly


class UserViewSet(viewsets.ModelViewSet):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminOrIsCurrentUserOrReadOnly]

