from django.conf.urls import url
from work import views

urlpatterns=[
    url('view_work/',views.view_work)
]