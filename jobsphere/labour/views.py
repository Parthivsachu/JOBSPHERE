from django.http import HttpResponse
from django.shortcuts import render
from labour.models import Labour
# Create your views here.
def manage_labour(request) :
    return render(request,'labour/manage_labour.html',)
from rest_framework.views import APIView,Response
from labour.serializers import android_serializer
class labour(APIView):
    def post (self,request):
        ob = Labour()
        ob.labour_id=1
        ob.username=request.data['username']
        ob.password=request.data['password']
        ob.address=request.data['address']
        ob.contact=request.data['contact']
        ob.email=request.data['email']
        ob.save()
        return HttpResponse('yes')
