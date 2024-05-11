from django.conf.urls import url
from pay_security import views

urlpatterns=[
    url('post_security/(?P<idd>\w+)/(?P<idd1>\w+)',views.post_security),
    url('view/',views.view_security)

]