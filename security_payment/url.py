from django.conf.urls import url
from security_payment import views

urlpatterns=[
    url('post_security/(?P<idd>\w+)/(?P<idd1>\w+)',views.post_security),
    url('update_security/(?P<idd>\w+)',views.update_security),
    url('add_security/',views.add_security),
    url('view_security/',views.view_security)

]