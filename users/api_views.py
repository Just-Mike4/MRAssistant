from rest_framework import viewsets
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class CustomUserViewset(viewsets.ModelViewSet):
    serializer_class=CustomUserSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    http_method_names=['put','get','delete']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = CustomUser.objects.filter(username=self.request.user)
            return user
        else:
            return CustomUser.objects.none()
    
    def update(self, request, *args, **kwargs):
        # Override the update method to handle PUT requests
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
