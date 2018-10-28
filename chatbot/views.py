from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json

def index(request):
    return render(request, 'index.html')

def message(request):
  return HttpResponse(json.dumps({'text': 'aaaa'}), content_type="application/json")
