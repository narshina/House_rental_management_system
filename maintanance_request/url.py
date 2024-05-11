from django.conf.urls import url
from maintanance_request import views

urlpatterns=[
    url('main_post/',views.post_main),
    url('view_main/',views.view_main),
    url('ps_rp/(?P<idd>\w+)',views.reply_main),
    url('aaaaaa/',views.view_reply)


]