from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'home - Главная', 
        'content': 'Магазин мебели HOME'
    }
    return render(request, 'main/index.html', context) 
def about(request):
    context = {
        'title': 'home - О нас',
        'content': 'О нас', 
        'text_on_page': 'У нас очень классный магазин, правда'
    }
    return render(request, 'main/about.html', context)