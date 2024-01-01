from rest_framework import viewsets
from .serializers import MoodDataSerializers
from .models import MoodData
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND,HTTP_200_OK
from rest_framework.authtoken.models import Token

class MoodDataViewSet(viewsets.ModelViewSet):
    serializer_class=MoodDataSerializers
    queryset=MoodData.objects.all()
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)