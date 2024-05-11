from django.conf.urls import url
from fedback_owner import views

urlpatterns=[
    url('feed_post/',views.post_feed),
    url('view_feed/',views.view_feed),
    url('abc/', views.post_feed_house),
    url('xxx/',views.view_feed_house),
    url('yy/',views.f_owner),
    url('public/',views.public)

]