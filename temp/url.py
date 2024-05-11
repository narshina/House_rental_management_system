from django.conf.urls import url
from temp import views


urlpatterns=[
    url('admin/',views.admin),
    url('home/',views.home),
    url('tenant/',views.tenanthome),
    url('owner/',views.ownerhome),
    url('mainhm/', views.mainhome),
    url('maionr/',views.mainonr),
    url('mainadmn/',views.mainadmin),
    url('maintnant/',views.maintnant)
]
