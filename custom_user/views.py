from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from .serializers import UserSerializer
from .models import CustomUser

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    lookup_field = 'username'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().partial_update(request, *args, **kwargs)
    
    def update(self, request, username=None):
        password = request.data.get('password', None)
        print(f"pass: {password}")
        if password: 
            return Response({
                    "error": 'It\'s forbidden update the password, contact the admin please'
                }, status=status.HTTP_403_FORBIDDEN)
        profesional = get_object_or_404(CustomUser, username=username)
        serializer = self.get_serializer(profesional, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            self.perform_update(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def create(self, request, *args, **kwargs):
        return Response({
            "error": 'It\'s forbidden to do this action'
        }, status=status.HTTP_403_FORBIDDEN)
    
    def destroy(self, request, *args, **kwargs):
        return Response({
            "error": 'It\'s forbidden to do this action'
        }, status=status.HTTP_403_FORBIDDEN)
    
    

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request: Request):

    user = get_object_or_404(CustomUser, username=request.data['username'])

    if not user.check_password(request.data['password']):
        return Response({
            "error": "Invalid password"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    refresh = RefreshToken.for_user(user)
    serializer = UserSerializer(instance=user)

    return Response({
        "token": str(refresh.access_token), 
        "token_refresh": str(refresh),
        "user": serializer.data
    }, status=status.HTTP_200_OK)