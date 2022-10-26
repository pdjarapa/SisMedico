#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args,**kwargs):
	print (args, kwargs)
	print (request)
	print (request.user)
	return render(request, "home.html", {})
	#return HttpResponse("<h1>Hola Bienvenido al Sistema appUno</h1>")

def about_view(request):
	return render(request, "about.html", {})

def contact_view(request,):
	return render(request, "contact.html", {})