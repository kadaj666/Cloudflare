from rest_framework import viewsets
from rest_framework import permissions
from .models import cloudflareAccount
from .serializers import  AccountSerializer


class Account(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = cloudflareAccount.objects.all()
    serializer_class = AccountSerializer
    http_method_names = ['get', 'delete', 'patch', 'post', 'options']

