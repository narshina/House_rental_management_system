from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')

def home(request):
    return render(request,'temp/home.html')

def tenanthome(request):
    return render(request,'temp/tenanthome.html')

def ownerhome(request):
    return render(request,'temp/ownerhome.html')

def mainhome(request):
    return render(request,'temp/mainhome.html')

def mainonr(request):
    return render(request,'temp/mainowner.html')

def mainadmin(request):
    return render(request,'temp/mainadmin.html')

def maintnant(request):
    return render(request,'temp/maintenant.html')
