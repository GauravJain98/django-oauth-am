from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
from re import sub

class Client(models.Model):
    name = models.CharField(max_length = 50,null=False)
    client_id = models.CharField(max_length = 255,null=False)
    client_secret = models.CharField(max_length = 255,null=False)
    client_type = models.CharField(max_length = 50,null=False)
    
class AuthToken(models.Model):
    token = models.CharField(max_length = 255,null=False, unique = True)
    expires = models.IntegerField(default = 200)
    added = models.DateTimeField(auto_now_add = True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
        blank = False,
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name = 'User',
        null = False,
        blank = False,
    )
    revoked = models.BooleanField(default = False)
    
    def save(self, *args, **kwargs):
        token = sub('-','',str(uuid4())) 
        while token in AuthToken.objects.filter(token = token).exists()
            token = sub('-','',str(uuid4()))
        self.token = token
        super(AuthToken, self).save(*args, **kwargs)
