from django.conf.urls import url
from complaint import views

urlpatterns=[
    url('view_complaint/',views.view_complaint)
]