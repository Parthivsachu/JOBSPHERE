from django.conf.urls import url
from labour import views

urlpatterns=[
    url('manage_labour/',views.manage_labour)
]