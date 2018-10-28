from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')

def message(request):
  responseData = {
    'text' : "hiiiiiiiiiii"
  }

  return JsonResponse(responseData)
