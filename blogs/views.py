# Create your views here.
# from django.shortcuts import render, HttpResponse
# def index(request):
#     return HttpResponse("Hola Mundo!")

# def adios(request):
#     return HttpResponse("¡Chao Pescao!")

# def saludar(request, name):
#     respuesta = "Muy buenos días" + name
#     return HttpResponse(respuesta)

# def age(request, age):
#     respuesta = f"la edad de {name}  es de {edad} años"
#     return HttpResponse(respuesta)

from django.shortcuts import HttpResponse, redirect # agrega redirección a la declaración de importación
def some_method(request):
	return redirect("/") 

def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request, new):
    return HttpResponse("placeholder para un nuevo formulario para crear un nuevo blogs")

def create(request, create):
    return redirect("/")

def show(request, number):
    respuesta = f"placeholder para mostrar el blog numero: {number}"
    return HttpResponse(respuesta)

def edit(request, number, edit):
    respuesta = f" placeholder para editar el blog {number}"
    return HttpResponse(respuesta)

def destroy(request, number,delete):
    return redirect("/")

