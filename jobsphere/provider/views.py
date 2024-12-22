from django.http import HttpResponse
from django.shortcuts import render
from provider.models import Provider
# Create your views here.
from rest_framework.views import APIView,Response
from provider.serializers import android_serializer


class provider(APIView):
    def post(self, request):
        ob = Provider()
        ob.provider_id = 1
        ob.username = request.data['username']
        ob.password = request.data['password']
        ob.address = request.data['address']
        ob.contact = request.data['contact']
        ob.email = request.data['email']
        ob.save()
        return HttpResponse('yes')
from django.shortcuts import render

# Create your views here.
