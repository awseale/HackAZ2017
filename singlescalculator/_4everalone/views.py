from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, '_4everalone/mywebsite.html')

def contact(request):
	return render(request, '_4everalone/')
