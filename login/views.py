from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render
from login.models import Login

# Create your views here.


def post_login(request):
    if request.method=="POST":
        name = request.POST.get("uname")
        password=request.POST.get("psw")
        obj = Login.objects.filter(username=name,pasword=password)
        tp = ""
        for ob in obj:
            tp=ob.type
            uid=ob.uid
            if tp =="admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp =="tenant":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/tenant/')
            elif tp =="owner":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/owner/')
        else:
            objilist="incorrect username or password.....please try again...!"
            context={
                'msg':objilist,
            }
            return render(request, 'login/login.html',context)


    return render(request, 'login/login.html')

