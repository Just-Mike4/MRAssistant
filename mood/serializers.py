from rest_framework import serializers
from .models import MoodData

class MoodDataSerializers(serializers.ModelSerializer):
    class Meta:
        model=MoodData
        fields='__all__'