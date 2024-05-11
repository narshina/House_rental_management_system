from django.shortcuts import render
from pay_rent.models import PayRent
from rent_payment.models import RentPayment

# Create your views here.


def post_rent(request,idd,idd1):
    obb = RentPayment.objects.get(add_rent_id=idd)
    context = {
        's': obb
    }
    cc=request.session["uid"]
    if request.method=='POST':
        obj=PayRent()
        obj.name=request.POST.get('name')
        obj.card_no=request.POST.get('cardnumber')
        obj.cvv=request.POST.get('cvv')
        obj.amount=request.POST.get('amount')
        obj.tenant_id=cc
        obj.owner_id=idd1
        obj.add_rent_id=idd
        obj.status='paid'
        obj.save()
    return render(request, 'pay_rent/rent_payment.html',context)

def view_rent(request):
    ss = request.session["uid"]
    obj=PayRent.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request,'pay_rent/view_rent_sts.html',context)



