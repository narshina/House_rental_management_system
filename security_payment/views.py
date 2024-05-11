from django.shortcuts import render
from security_payment.models import SecurityPayment
from tenant.models import Tenant
from owner.models import Owner
from property.models import Property

# Create your views here.


def post_security(request,idd,idd1):
    ob = Property.objects.get(house_id=idd)
    context = {
        'x': ob,
    }
    ss=request.session["uid"]
    if request.method=='POST':
        obj=SecurityPayment()
        obj.house_id = idd
        obj.tenant_id=idd1
        obj.owner_id=ss
        obj.amount=request.POST.get('amount')
        obj.duedate=request.POST.get('duedate')
        obj.save()
    return render(request, 'security_payment/add_securitypay.html',context)

def update_security(request,idd):
    obj = SecurityPayment.objects.get(add_security_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=SecurityPayment.objects.get(add_security_id=idd)
        obj.amount=request.POST.get('housename')

        obj.save()
        return add_security(request)
    return render(request, 'security_payment/update_security2.html',context)

def add_security(request):
    ss = request.session["uid"]
    obj=SecurityPayment.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request, 'security_payment/update_securitypay.html',context)

def view_security(request):
    ss = request.session["uid"]
    obj=SecurityPayment.objects.filter(tenant_id=ss)
    context={
        'x':obj
    }
    return render(request, 'security_payment/view_securitypay.html',context)

