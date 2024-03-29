from .serializers import UserRegistrationSerializer, LoginSerializer, LogoutSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.contrib.auth import authenticate, logout
from django.contrib import messages
from rest_framework_simplejwt.exceptions import TokenError
from django.shortcuts import render, HttpResponse, redirect
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.signals import user_logged_in, user_logged_out

@swagger_auto_schema(method="post",request_body=UserRegistrationSerializer())
@api_view(['POST'])
def user_registration(request):
    '''
    This is the register
    '''
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            data = {}
            user = serializer.save()
            data['Success'] = 'User has been created'
            data['username'] = user.username
            data['email'] = user.email
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@swagger_auto_schema(method="post",request_body=LoginSerializer())
@api_view(['POST'])
def user_login(request):
    if request.method == "POST":
        
        serializer = LoginSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(request, username = serializer.validated_data['username'], password = serializer.validated_data['password'])
        if user:
            if user.is_active:
                try:
                    refresh = RefreshToken.for_user(user)
                    
                    user_details = {}
                    user_details['id']   = user.id
                    user_details['username'] = user.username
                    user_details['email'] = user.email
                    user_details['refresh_token'] = str(refresh)
                    user_details['access_token'] = str(refresh.access_token)
                    user_logged_in.send(sender=user.__class__,
                                        request=request, user=user)

                    data = {
                    'message' : "success",
                    'data' : user_details,
                    }
                    return Response(data, status=status.HTTP_200_OK)


                except Exception as e:
                    raise e
            
            else:
                data = {
                    'message'  : "failed",
                    'errors': 'This account is not active'
                    }
                return Response(data, status=status.HTTP_403_FORBIDDEN)


        else:
            data = {
                'message'  : "failed",
                'errors': 'Please provide a valid username and password'
                }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)



@swagger_auto_schema(method="post",request_body=LogoutSerializer())
@api_view(["POST"])
def logout_view(request):
    """Log out a user by blacklisting their refresh token then making use of django's internal logout function to flush out their session and completely log them out.
    Returns:
        Json response with message of success and status code of 204.
    """
    
    serializer = LogoutSerializer(data=request.data)
    
    serializer.is_valid()
    
    try:
        token = RefreshToken(request.data.get('refresh'))
        token.blacklist()
        # token = RefreshToken(token=serializer.validated_data["refresh_token"])
        # token.blacklist()
        user=request.user
        user_logged_out.send(sender=user.__class__,
                                        request=request, user=user)
        logout(request)
        
        return Response({"message": "success"}, status=status.HTTP_204_NO_CONTENT)
    except TokenError:
        return Response({"message": "failed", "error": "Invalid refresh token"}, status=status.HTTP_400_BAD_REQUEST)