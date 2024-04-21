"""
URL configuration for iws backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from account.views import (
    AuthViewSet,
    UserViewSet
)
from chat.views import (
    UserMessageViewSet,
    SessionViewSet
)


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'sessions', SessionViewSet)
router.register(r'user-messages', UserMessageViewSet)

auth_router = routers.DefaultRouter()
auth_router.register(r'', AuthViewSet, basename='auth')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include(auth_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
