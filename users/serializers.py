from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.ModelSerializer):
    id=serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model=CustomUser
        fields=['id','username','email','date_of_birth']
    
    def get_id(self,obj):

        return obj.id