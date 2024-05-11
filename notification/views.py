from django.shortcuts import render
from notification.models import Notification
import datetime
from owner.models import Owner
from tenant.models import Tenant

# Create your views here.

def post_not(request):
    obj=Tenant.objects.all()
    context={
        'x':obj
    }
    ss=request.session["uid"]
    if request.method=='POST':
        obj=Notification()
        obj.owner_id=ss
        obj.tenant_id=request.POST.get('tname')
        obj.notification=request.POST.get('notification')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.save()
    return render(request, 'notification/add_notification.html',context)

def view_not(request):
    ss=request.session["uid"]
    obj=Notification.objects.filter(tenant_id=ss)
    context={
        'x':obj
    }
    return render(request,'notification/view_notification.html',context)