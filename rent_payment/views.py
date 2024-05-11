from django.shortcuts import render
from rent_payment.models import RentPayment
from tenant.models import Tenant
from owner.models import Owner
from property.models import Property
# Create your views here.


def post_rent(request,idd,idd1):
    ob=Property.objects.get(house_id=idd)
    context={
        'x':ob,
    }
    aa=request.session["uid"]
    if request.method=='POST':
        obj=RentPayment()
        obj.house_id = idd
        obj.tenant_id=idd1
        obj.owner_id=aa
        obj.rent_amount=request.POST.get('amount')
        obj.due_date=request.POST.get('due date')
        obj.save()
    return render(request,'rent_payment/add_rent.html',context)

def update_rent(request):
    ss=request.session["uid"]
    obj=RentPayment.objects.filter(owner_id=ss)
    context={
        'y':obj
    }
    return render(request,'rent_payment/update_rent.html',context)

def add_rent(request,idd):
    obj = RentPayment.objects.get(add_rent_id=idd)
    context = {
        'y': obj
    }
    if request.method=='POST':
        obj=RentPayment.objects.get(add_rent_id=idd)
        obj.rent_amount=request.POST.get('housename')
        obj.save()
        return update_rent(request)
    return render(request,'rent_payment/update_rent2.html',context)

def view_rent(request):
    ss = request.session["uid"]
    obj=RentPayment.objects.filter(tenant_id=ss)
    context={
        'x':obj
    }
    return render(request,'rent_payment/view_rent.html',context)




