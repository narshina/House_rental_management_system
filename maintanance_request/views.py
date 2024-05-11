from django.shortcuts import render
from maintanance_request.models import MaintananceRequest
from property.models import Property
from owner.models import Owner
from tenant.models import Tenant
from property.models import Property
from owner.models import Owner

# Create your views here.


def post_main(request):
    bb=request.session["uid"]
    obj1=Property.objects.all()
    obj2=Owner.objects.all()
    context={
        'x':obj1,
        'y':obj2
    }
    if request.method=='POST':
        obj=MaintananceRequest()
        obj.tenant_id=bb
        obj.house_id=request.POST.get('hname')
        obj.owner_id=request.POST.get('oname')
        obj.maintanance=request.POST.get('maintanance')
        obj.reply='pending'
        obj.save()
    return render(request,'maintanance_request/maintanance_request.html',context)


def view_main(request):
    ss=request.session["uid"]
    obj=MaintananceRequest.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request,'maintanance_request/view_maintanance.html',context)

def reply_main(request,idd):
    if request.method=='POST':
        obj=MaintananceRequest.objects.get(maintanance_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        return view_main(request)
    return render(request,'maintanance_request/reply_maintanance.html')

def view_reply(request):
    ss = request.session["uid"]
    obj=MaintananceRequest.objects.filter(tenant_id=ss)
    context={
        'x':obj
    }
    return render(request,'maintanance_request/view_reply.html',context)

