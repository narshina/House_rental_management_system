from django.conf.urls import url
from rent_payment import views

urlpatterns=[
    url('post_rent/(?P<idd>\w+)/(?P<idd1>\w+)',views.post_rent),
    url('update_rent/',views.update_rent),
    url('add_rent/(?P<idd>\w+)',views.add_rent),
    url('view_rent/',views.view_rent)

]