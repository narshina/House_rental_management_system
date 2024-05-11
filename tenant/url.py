from django.conf.urls import url
from tenant import views

urlpatterns=[
    url('post_tenant/',views.post_tenant),
    url('manage_tenant/',views.manage_tenant),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject)


]