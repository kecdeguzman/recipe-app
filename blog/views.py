from django.shortcuts import render
from django.http import HttpResponse

import requests

def index(request):
    query = "beef"
    response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+query+"&app_id=acf4c64c&app_key=d5a5df9dd27b9d8a69194531e80d79c0")
    jsonResponse = response.json()
    recipes = jsonResponse['hits']
    return render(request, 'blog/index.html', {'recipes' : recipes})

def specific(request):
    return HttpResponse('Second nito')

def article(request, article_id):
    return HttpResponse(article_id)

def search(request):
    if request.method == "POST":
        userText = request.POST.get('userText')
        response = requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+userText+"&app_id=acf4c64c&app_key=d5a5df9dd27b9d8a69194531e80d79c0")
        jsonResponse = response.json()
        recipes = jsonResponse['hits']
        return render(request, 'blog/index.html', {'recipes' : recipes})
    else:
        return render(request, "blog/index.html")