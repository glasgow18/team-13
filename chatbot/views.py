from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from tensorflow import setup as tf

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def message(request):
  if request.method == "POST":

    # PLUG IN BOT HERE!
    botresponse = tf.setupout(request.data)
    return HttpResponse(json.dumps({'text': botresponse}), content_type="application/json")
