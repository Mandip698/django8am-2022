from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/home/index.html')


def about(request):
    data={
        'title':"About Us"
    }    
    return render(request,'pages/about/about.html',data)


def contact(request):
    data={
        'title':"Contact Us"
    } 
    return render(request,'pages/contact/contact.html',data)