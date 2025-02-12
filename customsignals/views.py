from django.shortcuts import render,HttpResponse
from customsignals import signals
# Create your views here.
def home(request):
    signals.notification.send(sender=None,request=request,user="swet")
    return HttpResponse("this is home page")