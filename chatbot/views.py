from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def message(request):
  if request.method == "POST":

    # PLUG IN BOT HERE!
    botresponse = "geez a response"
    return HttpResponse(json.dumps({'text': botresponse}), content_type="application/json")
