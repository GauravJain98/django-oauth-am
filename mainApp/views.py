from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

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
                AuthToken(client = client,user = user)
                AuthToken.save()
        else:
            err = 'invalid client'
    if err:
        return Response({'error/s':err})
    else:


@api_view(['POST'])
def revoke(request):
    return Response()