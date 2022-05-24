from django.shortcuts import get_object_or_404,render,redirect
from . models import Blogger
from . forms import contactForm
def home(request):
    blog = Blogger.objects.all()
    context={'b':blog}
    return render(request,"blogger/index.html",context)

def about(request):
    context={}
    return render(request,"blogger/about-us.html",context)

def contact(request):
    form = contactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form =contactForm()
    context={"form":form}
    return render(request,"blogger/forms.html",context)

def listblog(request):
    blog = Blogger.objects.all()
    context={'b':blog}
    return render(request,"blogger/list.html",context)

def create(request):
    blog = Blogger.objects.all()
    context={'b':blog}
    return render(request,"blogger/create.html",context)

def details(request , slug):
    #blog = Blogger.objects.get(pk=blog_id)

    blog =get_object_or_404(Blogger,slug = slug)
    context={'b':blog}
    return render(request,"blogger/details.html",context)

def delete(request , slug):
    #blog = Blogger.objects.get(pk=blog_id)

    blog =get_object_or_404(Blogger,slug = slug)
    context={'b':blog}
    return render(request,"blogger/form.html",context)

def update(request , slug):
    #blog = Blogger.objects.get(pk=blog_id)
    #p = Blogger.objects.get(slug = slug)

    blog =get_object_or_404(Blogger,slug = slug)
    context={'b':blog}
    return render(request,"blogger/update.html",context)
