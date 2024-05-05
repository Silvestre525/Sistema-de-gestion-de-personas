from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index():


    return render (request, '/apps/compra/templates/index.html'), {

        'title': 'Compra'
    }