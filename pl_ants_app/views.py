from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Hello, world. You're at the pl_ants index.")
    return render(request, 'home.html', context={})

def base_page(request):
    context = {
        'plant_1': '0',
        'plant_2': '50',
        'plant_3': '85',
        'plant_4': '22',
        'plant_5': '100',
        'plant_6': '100',
    }
    return render(request, 'base.html', context=context)
