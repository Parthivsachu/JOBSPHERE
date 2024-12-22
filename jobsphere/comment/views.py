from django.http import HttpResponse
from django.shortcuts import render
from comment.models import Comment
# Create your views here.
def view_comment(request):

    return render(request,'comment/view_comment.html')

from rest_framework.views import APIView,Response
from comment.serializers import android_serializer

import datetime

class comment(APIView):
    def post (self,request):
        ob=Comment()
        ob.provider_id=1
        ob.description=request.data['description']
        ob.consumer_id=1
        ob.date = datetime.datetime.now()
        ob.save()
        return HttpResponse('yes')