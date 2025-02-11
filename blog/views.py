from django.shortcuts import render,HttpResponse

# Create your views here.

def sign(request):
    a=10/0
    return HttpResponse("hello")