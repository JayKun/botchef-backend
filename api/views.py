from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index(request):
    response_data = {}
    response_data['result'] = 'error'
    response_data['message'] = 'Some error message'
    return JsonResponse(response_data)