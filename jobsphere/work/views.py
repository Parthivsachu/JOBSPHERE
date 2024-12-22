from django.http import HttpResponse
from django.shortcuts import render
from work.models import Work
# Create your views here.
def view_work(request):
    return render (request,'work/view_work.html',)
from rest_framework.views import APIView,Response
from work.serializers import android_serializer
class work(APIView):
    def post(self, request):
        ob = Work()
        ob.work_id=1
        ob.provider_id=1
        ob.image=request.data['image']
        ob.description=request.data['description']
        ob.save()
        return HttpResponse('yes')