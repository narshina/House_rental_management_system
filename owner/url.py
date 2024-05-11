from django.conf.urls import url
from owner import views

urlpatterns=[
    url('post_owner/',views.post_owner),
    url('manage_owner/',views.manage_owner),
    url('apprvv/(?P<idd>\w+)', views.apprv),
    url('reject/(?P<idd>\w+)',views.reject)

]