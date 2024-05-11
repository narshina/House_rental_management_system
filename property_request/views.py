from django.shortcuts import render
from property_request.models import PropertyRequest
import datetime
from tenant.models import Tenant
from property.models import Property

# Create your views here.


def post_proprqst(request,idd,idd1):
    nn=request.session["uid"]
    if request.method=='POST':
        obj=PropertyRequest()
        obj.tenant_id=nn
        obj.house_id=idd
        obj.owner_id=idd1
        obj.required_year=request.POST.get('time period')
        obj.required_month=request.POST.get('month')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.reply='pending'
        obj.save()
    return render(request,'property_request/propert_request.html')

def reply_proprqst(request,idd):
    if request.method=='POST':
        obj=PropertyRequest.objects.get(request_id=idd)
        obj.reply=request.POST.get('reply')
        obj.save()
        return view_proprqst(request)
    return render(request,'property_request/reply_requestproperty.html')

def view_proprqst(request):
    ss = request.session["uid"]
    obj=PropertyRequest.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request,'property_request/view_propertyrequest.html',context)


def dlttt(request,idd):
    obj=PropertyRequest.objects.get(request_id=idd)
    obj.delete()
    return view_proprqst(request)

def view_reply(request):
    ss = request.session["uid"]
    obj=PropertyRequest.objects.filter(tenant_id=ss)
    context={
        'x':obj
    }
    return render(request,'property_request/view_reply.html',context)

def add_sec(request):
    ss=request.session["uid"]
    obj=PropertyRequest.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request,'property_request/add_security_pay.html',context)

def rent_pay(request):
    ss = request.session["uid"]
    obj=PropertyRequest.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request,'property_request/add_rent_payment.html',context)