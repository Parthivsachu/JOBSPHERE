from rest_framework import serializers
from skill.models import Skill

class android_serializer(serializers.ModelSerializer):
    class Meta:
        model=Skill
        fields='__all__'