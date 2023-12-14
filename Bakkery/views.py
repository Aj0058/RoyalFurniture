from django.shortcuts import render, redirect, HttpResponse
from .models import Image
from .forms import ImageSearchForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

def Homes(request):
    return render(request, "home.html")

def Abouts(request):
    return render(request, "AboutUs.html")

def Light(request):
    return render(request, 'Lights.html')

def Page(request):
    return render(request, 'paginator.html')

def Cost1(request):
    return render(request, 'Cost1.html')

def Cost2(request):
    return render(request, 'Cost2.html')

def Cost3(request):
    return render(request, 'Cost3.html')

def Cost4(request):
    return render(request, 'Cost4.html')

def Chandle(request):
    return render(request, 'Chandle.html')

def Lamps(request):
    return render(request, 'Lamp.html')

def Hang(request):
    return render(request, 'Hang.html')

def Out(request):
    return render(request, 'Outdoor.html')

def Bed(request):
    return render(request, 'Beds.html')

def Chair(request):
    return render(request, 'Chair.html')

def Stool(request):
    return render(request, 'Stool.html')

def Swing(request):
    return render(request, 'Swing.html')

def Picture(request):
    return render(request, 'PIC.html')

def Wall(request):
    return render(request, 'Wall.html')

def Tasks(request):
    return render(request, 'Tasks.html')

def Table(request):
    return render(request, 'Table.html')

def Almira(request):
    return render(request, 'Almira.html')

def Floor1(request):
    return render(request, 'Floor1.html')

def Floor2(request):
    return render(request, 'Floor2.html')

def Floor3(request):
    return render(request, 'Floor3.html')

def Hang1(request):
    return render(request, 'Hang1.html')

def Hang2(request):
    return render(request, 'Hang2.html')

def Hang3(request):
    return render(request, 'Hang3.html')

def Out1(request):
    return render(request, 'Out1.html')

def Out2(request):
    return render(request, 'Out2.html')

def Out3(request):
    return render(request, 'Out3.html')

def Contact(request):
    return render(request, 'ContactUs.html')

def Crouch(request):
    return render(request, 'Crouch.html')

def Blog(request):
    return render(request, 'Blog.html')

def Ragister(request):
    if request.method == "POST":
        name = request.POST.get('username')
        Email = request.POST.get('Email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and Confirm Password are not matching")
        else:
            my_user = User.objects.create_user(name, Email, pass1)
            my_user.save()
            return redirect('Log')

    return render(request, "Ragister.html")

def Login(request):
    if request.method == 'POST':
        Name = request.POST.get('Name')
        password = request.POST.get('password')
        user = authenticate(request, username=Name, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Your Username and Password is Incorrect")
    
    return render(request, 'Login.html')

# def image_search(request):
#     images = Image.objects.all()
#     form = ImageSearchForm(request.GET)
#     search_query = request.GET.get('search_query', '')
#
#     if search_query:
#         images = images.filter(title__icontains=search_query)
#
#     context = {
#         'images': images,
#         'form': form,
#         'search_query': search_query,
#     }
#
#     return render(request, 'image_search.html', context)
