from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length = 50,null=False)
    client_id = models.CharField(max_length = 255,null=False)
    client_secret = models.CharField(max_length = 255,null=False)
    client_type = models.CharField(max_length = 50,null=False)
    
class AuthToken(models.Model):
    token = models.CharField(max_length = 255,null=False)
    expires = models.IntegerField(default = 200)
    added = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
        blank = False,
    )
    Client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
        blank = False,
    )
    revoked = models.BooleanField(default = False)
