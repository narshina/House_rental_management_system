from django.shortcuts import render
from property.models import Property
from type.models import Type
from owner.models import Owner
from django.core.files.storage import FileSystemStorage

# Create your views here.


def post_prop(request):
    ss=request.session["uid"]
    obb=Type.objects.all()
    context={
        'xx':obb
    }
    if request.method=='POST':
        obj=Property()
        obj.owner_id=ss
        obj.type_id=request.POST.get('ty')
        obj.house_name=request.POST.get('house name')
        obj.owner_name=request.POST.get('owner name')
        obj.location=request.POST.get('location')
        obj.district=request.POST.get('district')
        obj.landmark=request.POST.get('landmark')
        obj.number_of_bedrooms=request.POST.get('number of bedroom')
        obj.area_of_house=request.POST.get('area of house')
        # obj.image1=request.POST.get('image1')
        myfile=request.FILES['image1']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.image1=myfile.name
        # obj.image2=request.POST.get('image2')
        myfile = request.FILES['image2']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        obj.image2 = myfile.name
        obj.security_payment=request.POST.get('security pay')
        obj.rent_amount=request.POST.get('rent amount')
        obj.status=request.POST.get('satus')
        obj.contact_no=request.POST.get('contact number')
        obj.block='pending'
        obj.save()
    return render(request, 'property/property.html',context)

def view_prop(request):
    if request.method=='POST':
        vv=request.POST.get('search')
        obj=Property.objects.filter(district__icontains=vv)
        contex = {
            'x': obj
        }
        return render(request, 'property/view_property.html', contex)
    else:

        obj=Property.objects.filter(block='pending')
        contex={
            'x':obj
        }
    return render(request, 'property/view_property.html',contex)


def update_view(request):
    obj=Property.objects.filter(block='pending')
    context={
        'y':obj
    }
    return render(request, 'property/view_update_property.html',context)

def updates_prop(request,idd):
    obj = Property.objects.get(house_id=idd)
    context = {
        'y': obj
    }
    if request.method=='POST':
        obj=Property.objects.get(house_id=idd)
        obj.house_name=request.POST.get('housename')
        # obj.owner_name=request.POST.get('ownername')
        obj.location=request.POST.get('location')
        obj.district=request.POST.get('district')
        obj.landmark=request.POST.get('landmark')
        obj.number_of_bedrooms=request.POST.get('numberbedroom')
        obj.area_of_house=request.POST.get('areahouse')
        obj.security_payment=request.POST.get('securitypay')
        obj.rent_amount=request.POST.get('rentamount')
        obj.status=request.POST.get('status')
        obj.contact_no=request.POST.get('contactnumber')
        obj.save()
        return update_view(request)
    return render(request, 'property/update_property.html',context)


def dlttt(request,idd):
    obj=Property.objects.get(house_id=idd)
    obj.delete()
    return update_view(request)

def view_admn(request):
    obj=Property.objects.all()
    contex={
        'z':obj
    }
    return render(request,'property/view_admin.html',contex)


def blk(request,idd):
    obj=Property.objects.get(house_id=idd)
    obj.block='blocked'
    obj.delete()
    return view_admn(request)

def view_onr(request):
    ss=request.session['uid']
    obj=Property.objects.filter(block='pending',owner_id=ss)
    context={
        'w':obj
    }
    return render(request,'property/view_owner.html',context)