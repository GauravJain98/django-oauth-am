from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def index(request):
    params = {
        'somerthin':{
            'key':'value'
        },
        'somerthin1':'value',
        'somerthin2':'value',
        'somerthin3':'value',
    }
    return JsonResponse(params)