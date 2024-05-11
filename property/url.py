from django.conf.urls import url
from property import views

urlpatterns=[
    url('post_prop/',views.post_prop),
    url('view_prop/',views.view_prop),
    url('update_view/',views.update_view),
    url('up_prop/(?P<idd>\w+)',views.updates_prop),
    url('dlt/(?P<idd>\w+)',views.dlttt),
    url('bkk/(?P<idd>\w+)',views.blk),
    url('view_admn/',views.view_admn),
    url('view_onr/',views.view_onr)

]