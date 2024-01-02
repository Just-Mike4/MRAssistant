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
from .serializers import MoodDataSerializers
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserRegistrationSerializer

class MoodDataViewSet(viewsets.ModelViewSet):
    serializer_class=MoodDataSerializers
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    queryset=MoodData.objects.all()
    http_method_names=['put','get','delete','post']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_mood = MoodData.objects.filter(user=self.request.user)
            return user_mood
        else:
            return MoodData.objects.none()
        
    def perform_create(self, serializer):
        
        return serializer.save(user=self.request.user)


class Login(APIView):
    def post(self, request):
        user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
        if not user:
            return Response({'error': 'Credentials are incorrect or user does not exist'}, status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=HTTP_200_OK)
    

class UserRegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

