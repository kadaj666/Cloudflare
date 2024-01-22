from django.db import models

class cloudflareAccount(models.Model):
    name = models.CharField(max_length=100 ,null=True, blank=True)
    login = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.name
    
  