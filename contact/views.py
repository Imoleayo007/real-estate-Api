from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Contact
# from myapp.models import Listing
from .seriaizers import  Contact_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action,api_view
from django.contrib import messages 
from django.core.mail import send_mail

# Create your views here.


@swagger_auto_schema(method="POST", request_body=Contact_Serializer())
@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        serializer = Contact_Serializer(data=request.data)
        if serializer.is_valid():
            data = {}
            user = serializer.save()

            data['Success'] = 'successful Inquiry'
            data['name'] = user.name
            data['email'] = user.email
            data['message'] = user.message
            data['owner_email'] = user.owner_email
            # send_mail
            # ('Example Subject', 'Example message', 'from@example.com', ['to@example.com'])
            send_mail(
            'Property Listing Inquiry',f'{user.message}',
            'Xammyp007.com@gmail.com',[f'{user.owner_email}']
            )
            print(user.message)
            messages.success(
            request, 'Your request has been submitted, a owner will get back to you soon.')
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
