from django.conf.urls import url
from property_request import views

urlpatterns=[
    url('post_proprqst/(?P<idd>\w+)/(?P<idd1>\w+)',views.post_proprqst),
    url('reply_proprqst/(?P<idd>\w+)',views.reply_proprqst),
    url('view_proprqst/',views.view_proprqst),
    url('view_reply/',views.view_reply),
    # url('view_main/',views.view_main),
    url('dltttttt/(?P<idd>\w+)',views.dlttt),
    url('add_sec/',views.add_sec),
    url('rent_pay/',views.rent_pay)

]