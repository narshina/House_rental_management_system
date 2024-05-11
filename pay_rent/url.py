from django.conf.urls import url
from pay_rent import views

urlpatterns=[
    url('post_rent/(?P<idd>\w+)/(?P<idd1>\w+)',views.post_rent),
    url('view_rent/',views.view_rent)

]