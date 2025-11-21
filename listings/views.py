from django.shortcuts import render

# Create your views here.
# listings/views.py
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'message': 'Listings API is working!',
        'endpoints': {
            'admin': '/admin/',
            'api_docs': '/swagger/',
            'redoc_docs': '/redoc/',
        }
    }
    return Response(api_urls)