from django.http import HttpResponse
from django.shortcuts import render
from skill.models import Skill

# Create your views here.
from rest_framework.views import APIView,Response
from skill.serializers import android_serializer
class skill(APIView):
    def post(self, request):
        ob = Skill()
        ob.consumer_id=1
        ob.description=request.data['description']
        ob.image=request.data['image']
        ob.save()
        return HttpResponse('yes')