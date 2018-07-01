from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['POST'])
def token(request):

    return Response()

@api_view(['POST'])
def revoke(request):
    return Response()