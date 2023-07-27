from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'first.html')
def second(request):
    return render(request,'second.html')
from django.http import HttpResponse
def third(request):
    return HttpResponse('Hloo how are you................')