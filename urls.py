from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'account', views.Account, 'account')


urlpatterns = [
    path('cloudflare/', include(router.urls)),
]
