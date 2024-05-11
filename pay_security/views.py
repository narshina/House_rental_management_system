from django.shortcuts import render
from pay_security.models import PaySecurity
from security_payment.models import SecurityPayment
from owner.models import Owner
# Create your views here.


def post_security(request,idd,idd1):
    vv=request.session["uid"]
    obb=SecurityPayment.objects.get(add_security_id=idd)
    context={
        's':obb
    }
    if request.method=='POST':
        obj=PaySecurity()
        obj.name=request.POST.get('housename')
        obj.card_no=request.POST.get('ownername')
        obj.cvv=request.POST.get('cvv')
        obj.amount=request.POST.get('amount')
        obj.add_security_id=idd
        obj.status='paid'
        obj.tenant_id=vv
        obj.owner_id=idd1
        obj.save()
    return render(request, 'pay_security/securitypay.html',context)

def view_security(request):
    ss = request.session["uid"]
    obj=PaySecurity.objects.filter(owner_id=ss)
    context={
        'x':obj
    }
    return render(request, 'pay_security/vie_security_sts.html',context)
