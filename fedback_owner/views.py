from django.shortcuts import render
from fedback_owner.models import FeedbackOwner
import datetime
from owner.models import Owner
from tenant.models import Tenant
from property.models import Property
# Create your views here.


def post_feed(request):
    ob=Owner.objects.all()
    context={
        'x':ob
    }
    ss=request.session["uid"]
    if request.method=='POST':
        obj=FeedbackOwner()
        obj.tenant_id=ss
        obj.feedback=request.POST.get('housename')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.owner_id=request.POST.get('oname')
        obj.house_id=1
        obj.type='owner'
        obj.save()
    return render(request, 'feedback_owner/add_ownerfeedback.html',context)


def view_feed(request):
    obj=FeedbackOwner.objects.filter(type='owner')
    context={
        'x':obj
    }
    return render(request, 'feedback_owner/view_ownerfeedback.html',context)


def post_feed_house(request):
    obj=Property.objects.all()
    context={
        'x':obj
    }
    aa=request.session["uid"]
    if request.method=='POST':
        obj=FeedbackOwner()
        obj.tenant_id=aa
        obj.feedback=request.POST.get('housename')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.now()
        obj.house_id=request.POST.get('hname')
        obj.owner_id=1
        obj.type='house'
        obj.save()
    return render(request, 'feedback_owner/add_housefeedback.html',context)

def view_feed_house(request):
    ss = request.session["uid"]
    obj=FeedbackOwner.objects.filter(type='house',owner_id=ss)
    context={
        'x':obj
    }
    return render(request, 'feedback_owner/view_housefeedback.html',context)

def f_owner(request):
    ss = request.session["uid"]
    obj=FeedbackOwner.objects.filter(type='owner',owner_id=ss)
    context={
        'x':obj
    }
    return render(request, 'feedback_owner/view_feedback_owner.html',context)

def public(request):
    obj=FeedbackOwner.objects.filter(type='house')
    context={
        'x':obj
    }
    return render(request, 'feedback_owner/public_feedback.html',context)


