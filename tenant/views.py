from django.shortcuts import render

from login.models import Login
from tenant.models import Tenant
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
# Create your views here.


def post_tenant(request):
    obk=""
    if request.method=='POST':
        a = request.POST.get('mobilenumber')
        b = request.POST.get('email')
        obv = Tenant.objects.filter(Q(mob_no=a) & (Q(email_id=b) | Q(mob_no=a) | Q(email_id=b)))
        if len(obv) > 0:
            obk = "User exist"
        else:
            obj=Tenant()
            obj.tenant_name=request.POST.get('name')
            obj.age=request.POST.get('age')
            obj.gender=request.POST.get('gender')
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
            # obj.professional_id=request.POST.get('professionalid')
            myfile = request.FILES['professionalid']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            obj.professional_id = myfile.name
            obj.status='pending'
            obj.marriage=request.POST.get('mar')
            obj.password=request.POST.get('pss')
            obj.save()

            ob = Login()
            ob.username = obj.email_id
            ob.pasword = obj.password
            ob.uid = obj.tenant_id
            ob.type = 'tenant'
            ob.save()
            obk = "Succefully Registered"
    context = {
                'msg': obk
            }
    return render(request, 'tenant/tenant.html',context)

def manage_tenant(request):
    obj=Tenant.objects.all()
    context={
        'x':obj,
    }
    return render(request,'tenant/manage_tenant.html',context)

def approve(request,idd):
    obj=Tenant.objects.get(tenant_id=idd)
    obj.status='approved'
    obj.save()
    return manage_tenant(request)

def reject(request,idd):
    obj=Tenant.objects.get(tenant_id=idd)
    obj.status='rejected'
    obj.save()
    return manage_tenant(request)
