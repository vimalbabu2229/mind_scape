from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

from .models import User
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer

# Manage user accounts details 
class AccountsViewSet(ViewSet):

    # Register new user with username, email and password. 
    @action(detail=False, methods=['post'])
    def register(self, request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                user = User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
                token, created = Token.objects.get_or_create(user=user)
                return Response({'data': RegisterSerializer(user).data, 'token': token.key }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            
     # Login user with username and password
    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                username = serializer.validated_data['username']
                password = serializer.validated_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token':token.key, 'username': user.username, 'email': user.email}, status=status.HTTP_200_OK)
                else :
                    return Response({'detail': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            else :
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Logout
    @action(detail=False, methods=['post'], permission_classes=[IsAuthenticated])    
    def logout(self, request):
        try:
            request.user.auth_token.delete()
            return Response({'detail':'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Delete account
    @action(detail=False, methods=['delete'], permission_classes=[IsAuthenticated]) 
    def delete(self, request):
        try :
            request.user.delete()
            return Response({'detail': 'User deleted successfully'}, status=status.HTTP_200_OK)

        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # Get user profile
    def _get_profile(self, request):
        serializer = ProfileSerializer(request.user, context={'request': request})

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Update profile details 
    def _update_profile(self, request):
        data = request.data
        if 'email' in  data :
            return Response({'detail': 'Not allowed to change email address'}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'username' in data:
            return Response({'detail': 'Not allowed to change username'}, status=status.HTTP_400_BAD_REQUEST)
        
        try :
            serializer = ProfileSerializer(request.user, data=data, partial=True, context={'request': request})
            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)
            
        except Exception as e :
            return Response({'detail': f'Something went wrong', 'exception': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # Manage user profile 
    @action(detail=False, methods=['get', 'patch'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        if request.method == "get":
            return self._get_profile(request)
        else:
            return self._update_profile(request)

