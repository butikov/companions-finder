"""companions_finder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import inc   lude, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework import routers
#from rest_framework.authtoken.views import obtain_auth_token

from meet.views import MeetViewSet
from user.views import UserViewSet
from comment.views import CommentViewSet
from core.views import index


router = routers.DefaultRouter()
router.register('meets', MeetViewSet)
router.register('users', UserViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('social_django.urls', namespace='social')),
    path('api/auth/', include('rest_framework.urls', namespace='api-auth')),
    path('api/v1/', include(router.urls)),
    re_path(r'^search/', include('haystack.urls')),
#    path('^api/token-auth/', obtain_auth_token),
    path('index/', index),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
