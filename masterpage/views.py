from django.shortcuts import render
from masterpage.models import Sports
from masterpage.models import Entertainment
from masterpage.models import Politics
from masterpage.models import Editorials

# Create your views here.
def masterpage(request):
    return render(request,'masterpage/master.html')

def gallery(request):
    return render(request,'masterpage/gallery.html')

def sports_view(request):
    sports=Sports.objects.all()
    return render(request,'masterpage/sports.html',{'sports':sports})


def entertainment_view(request):
    entertainment=Entertainment.objects.all()
    return render(request,'masterpage/entertainment.html',{'entertainment':entertainment})

def politics_view(request):
    politics=Politics.objects.all()
    return render(request,'masterpage/politics.html',{'politics':politics})

def editorials_view(request):
    editorials=Editorials.objects.all()
    return render(request,'masterpage/editorial.html',{'editorials':editorials})
