from rest_framework import serializers
from .models import cloudflareAccount

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = cloudflareAccount
        fields = ("__all__")


