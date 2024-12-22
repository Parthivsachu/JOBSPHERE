from django.http import HttpResponse
from django.shortcuts import render
from complaint.models import Complaint
# Create your views here.
def view_complaint(request) :

    return render(request,'complaint/view_complaint.html')
from rest_framework.views import APIView,Response
from complaint.serializers import android_serializer

import datetime

class complaint(APIView):
    def post (self,request):
        ob=Complaint()
        ob.provider_id=1
        ob.consumer_id=1
        ob.date=datetime.datetime.now()
        ob.description=request.data['description']
        ob.reply='text'
        ob.type=request.data['type']
        ob.save()
        return HttpResponse('yes')
