from django.shortcuts import render
from owner.models import Owner
from login.models import Login
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# Create your views here.


def post_owner(request):
    obk=""
    if request.method=='POST':
        a=request.POST.get('mobilenumber')
        b=request.POST.get('email')
        obv = Owner.objects.filter(Q(mob_no=a) & (Q(email_id=b) | Q(mob_no=a) | Q(email_id=b)))
        if len(obv) > 0:
            obk = "User exist"
        else:
            obj=Owner()
            obj.owner_name=request.POST.get('name')
            obj.age=request.POST.get('age')
            obj.gender=request.POST.get('gender')
            obj.password=request.POST.get('ps')
            obj.house_name=request.POST.get('housename')
            obj.landmark=request.POST.get('landmark')
            obj.district=request.POST.get('district')
            obj.pincode=request.POST.get('pincode')
            obj.mob_no=request.POST.get('mobilenumber')
            obj.email_id=request.POST.get('email')
            # obj.id_proof=request.POST.get('idproof')
            myfile=request.FILES['idproof']
            fs=FileSystemStorage()
            filename=fs.save(myfile.name,myfile)
            obj.id_proof=myfile.name
            obj.status='pending'
            obj.save()
            obk = "Succefully Registered"
    context = {
        'msg': obk
            }
    return render(request, 'owner/owner.html',context)

def manage_owner(request):
    obj=Owner.objects.all()
    context={
        'x':obj,
    }
    return render(request, 'owner/manage_owner.html',context)

def apprv(request,idd):
    obj=Owner.objects.get(owner_id=idd)
    obj.status='approved'
    obj.save()
    ob=Login()
    ob.username = obj.email_id
    ob.pasword = obj.password
    ob.uid = obj.owner_id
    ob.type = 'owner'
    ob.save()
    return manage_owner(request)

def reject(request,idd):
    obj=Owner.objects.get(owner_id=idd)
    obj.status='rejected'
    obj.save()
    return manage_owner(request)
