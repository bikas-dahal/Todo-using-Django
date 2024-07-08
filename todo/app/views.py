from django.shortcuts import render
from django.http import HttpResponse

from .rabbitmq import publish_message

def index(request):
    # publish_message('Message here!')
    # return HttpResponse("Hello, world. You're at the todo index. RabbitMQ")
    return render(request, 'index.html')