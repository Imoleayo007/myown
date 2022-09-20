from django.shortcuts import render
from .models import Sam
from django.shortcuts import render, redirect




def home(request):
    work = Sam.objects.all()
    return render(request, 'my_app/home.html',{'all_work': work})

def view(request):
    sams = Sam.objects.last()
    print(sams)
    return render(request,'my_app/view.html',{'sam' : sams})


