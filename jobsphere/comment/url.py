from django.conf.urls import url
from comment import views

urlpatterns=[
    url('view_cmt/',views.view_comment)
]