from django.http import HttpResponse
from django.shortcuts import render
from login.models import Login

# Create your views here.
def login(request) :
    return render(request,'login/login.html')
from rest_framework.views import APIView,Response
from login.serializers import android_serializer

class login(APIView):
    def post (self,request):
        ob = Login()
        ob.username=request.data['username']
        ob.password=request.data['password']
        ob.type=request.data['type']
        ob.login_id=1
        ob.u_id=1
        ob.save()
        return HttpResponse('yes')