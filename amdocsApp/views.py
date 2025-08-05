from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('this is home page')
def contact(request):
	return HttpResponse('this is contact me page')

