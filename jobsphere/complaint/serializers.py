from rest_framework import serializers
from complaint.models import Complaint

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Complaint
        fields='__all__'