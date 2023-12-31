from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser

class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class=CustomUserSerializer
    queryset=CustomUser.objects.all()
