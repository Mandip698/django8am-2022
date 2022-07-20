from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    data = {
        'newsData':News.objects.all(),
        'CategoryData':Category.objects.all(),
    }
    return render(request,'pages/home/index.html',data)


def about(request):
    data={
        'title':"About Us"
    }    
    return render(request,'pages/about/about.html',data)


def contact(request):
    data={
        'newsData':News.objects.all(),
        'title':"Contact Us"
    } 
    return render(request,'pages/contact/contact.html',data)


def news_details(request, slug):
    n_obj=News.objects.get(slug=slug)
    related_news=News.objects.filter(category=n_obj.category).exclude(slug=slug)
    n_obj.views += 1
    n_obj.save()
    data={
        'newsData':News.objects.get(slug=slug),
        'CategoryData':Category.objects.all(),
        'related_news':related_news,
    }
    return render(request,'pages/news/news_details.html',data)


def category(request,slug):
    data={
        'newsData':News.objects.filter(category__category_name=slug),
    }
    return render(request,'pages/news/category.html',data)