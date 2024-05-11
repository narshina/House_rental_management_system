from django.conf.urls import url
from notification import views

urlpatterns=[
    url('post_not/',views.post_not),
    url('view_not/',views.view_not)

]