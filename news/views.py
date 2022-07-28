from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import os
from django.utils.text import slugify

# Create your views here.


def index(request):
    data = {
        'newsData': News.objects.all(),
        'CategoryData': Category.objects.all(),
    }
    return render(request, 'pages/home/index.html', data)


def about(request):
    data = {
        'title': "About Us"
    }
    return render(request, 'pages/about/about.html', data)


def contact(request):
    data = {
        'newsData': News.objects.all(),
        'title': "Contact Us",
    }
    return render(request, 'pages/contact/contact.html', data)


def news_details(request, slug):
    n_obj = News.objects.get(slug=slug)
    related_news = News.objects.filter(
        category=n_obj.category).exclude(slug=slug)
    n_obj.views += 1
    n_obj.save()
    data = {
        'newsData': News.objects.get(slug=slug),
        'CategoryData': Category.objects.all(),
        'related_news': related_news,
    }
    return render(request, 'pages/news/news_details.html', data)


def category(request, slug):
    data = {
        'newsData': News.objects.filter(category__category_name=slug),
    }
    return render(request, 'pages/news/category.html', data)


def blog(request):
    data = {
        'blogsData': Blog.objects.all(),
        'title':"Blog",
    }
    return render(request, 'pages/blogs/blog.html', data)


def blog_details(request, slug):
    data = {
        'blogsData': Blog.objects.get(slug=slug),
        'title':"Blog",
    }
    return render(request, 'pages/blogs/blog_details.html', data)


def blog_add(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        intro = request.POST['intro']
        content = request.POST['content']
        slug = slugify(request.POST['title'])
        image = ''
        if request.FILES:
            image = request.FILES['image']
        Blog.objects.create(
            title=title, author=author, intro=intro, content=content, slug=slug, image=image
        )
        messages.success(request, 'Blog Added Successfully')
        return redirect('blog')
    else:
        data = {
            'blogsData': Blog.objects.all(),
            'title':"Blog",
        }
        return render(request, 'pages/blogs/blog_add.html', data)


def delete_file(slug):
    f_data = Blog.objects.get(slug=slug)
    if f_data.image:
        file_path = os.getcwd() + f_data.image.url
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            return True
    else:
        return True

# delete file function


def blog_delete(request, slug):
    if delete_file(slug) and Blog.objects.get(slug=slug).delete():
        messages.success(request, 'Blog Deleted Successfully')
        return redirect('blog')
    else:
        return redirect('blog')


def blog_update(request, slug):
    if request.method == "POST":
        bObj = Blog.objects.get(slug=slug)
        bObj.title = request.POST['title']
        bObj.author = request.POST['author']
        bObj.intro = request.POST.get('intro')
        bObj.content = request.POST.get('content')
        bObj.slug = slugify(request.POST['title'])
        image = ''
        if request.FILES:
            delete_file(slug)
            image = request.FILES['image']
        bObj.image = image
        bObj.save()
        messages.success(request, 'Blog Updated Successfully')
        return redirect('blog')
    else:
        data = {
            'title':"Blog",    
            'blogsData': Blog.objects.get(slug=slug)
        }
        return render(request, 'pages/blogs/blog_update.html', data)
