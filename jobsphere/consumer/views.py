from django.http import HttpResponse
from django.shortcuts import render
from consumer.models import Consumer
# Create your views here.
from rest_framework.views import APIView,Response
from consumer.serializers import android_serializer


class consumer(APIView):
    def post (self,request):
        ob = Consumer()
        ob.consumer_id=1
        ob.username=request.data['username']
        ob.password=request.data['password']
        ob.address=request.data['address']
        ob.contact=request.data['contact']
        ob.email=request.data['email']
        ob.save()
        return HttpResponse('yes')