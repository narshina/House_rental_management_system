from django.shortcuts import render
from type.models import  Type
from owner.models import Owner
from django.http import HttpResponseRedirect

# Create your views here.


def post_type(request):
    ss=request.session["uid"]
    if request.method=='POST':
        obj=Type()
        obj.owner_id=ss
        obj.type=request.POST.get('housename')
        obj.save()
        return HttpResponseRedirect('/property/post_prop/')
    return render(request, 'type/type.html')

