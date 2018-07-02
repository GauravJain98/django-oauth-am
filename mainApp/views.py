from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def token(request):
    data = request.data
    err = {}
    if 'client_id' not in data:
        err['client_id'] = 'required'
    if 'client_secret' not in data:
        err['client_secret'] = 'required'
    if 'username' not in data:
        err['username'] = 'required'
    if 'password' not in data:
        err['password'] = 'required'
    if err:
        return Response({'error/s':err})
    else:
        client = Client.objects.filter(client_id = data['client_id'],client_secret = data['client_secret'])
        if client.exists():
            user = authenticate(username=data['username'], password=data['password'])
            if user:
                token = AuthToken(client = list(client)[0],user = user)
                token.save()
                return Response({
                    'token':token.token,
                    'expires':token.expires,
                    'user':data['username']
                })
            else:
                err = 'invalid user'
        else:
            err = 'invalid client'
    return Response({'error/s':err})
 

@api_view(['POST'])
def revoke(request):
    data = request.data
    err = {}
    if 'client_id' not in data:
        err['client_id'] = 'required'
    if 'client_secret' not in data:
        err['client_secret'] = 'required'
    if 'token' not in data:
        err['token'] = 'required'
    if err:
        return Response({'error/s':err})
    else:
        client = Client.objects.filter(client_id = data['client_id'],client_secret = data['client_secret'])
        if client.exists():
            token = AuthToken.objects.filter(token = data['token'])
            if token.exists() and not token.first().revoked:
                token = list(token)[0]
                token.revoked = True
                token.save()
                return Response({'token':token.token,'revoked':True})
            else:
                err = 'already revoked'
        else:
            err = 'invalid client'
        return Response({'error/s':err})
