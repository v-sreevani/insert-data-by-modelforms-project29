from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            TFDO.save()
            return HttpResponse('Topic is insertd successfully')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    WFO=WebpageForm()
    d={'WFO':WFO}

    if request.method=='POST':
        WPFO=WebpageForm(request.POST)
        if WPFO.is_valid():
            WPFO.save()
            return HttpResponse('Wepage is inserted')

    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    AFO=AccessForm()
    d={'AFO':AFO}

    if request.method=='POST':
        AFDO=AccessForm(request.POST)
        if AFDO.is_valid():
            AFDO.save()
            return HttpResponse('Accessrecord is inserted')
            
    return render(request,'insert_accessrecord.html',d)
