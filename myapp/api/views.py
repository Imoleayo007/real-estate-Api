from django.shortcuts import render, redirect
from myapp.models import Listing
from .seriaizers import Listing_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action,api_view
from django.contrib.auth.decorators import login_required
from django.contrib import messages 


    
# class Editing(APIView):
@swagger_auto_schema(method="PUT", request_body=Listing_Serializer())
@api_view(["PUT"])
def put(request, advert_id):
    """Allows logged in users to edit all the details of a job advert at ones"""
    try:
        post = Listing.objects.get(id=advert_id)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        # posting = Listing.objects.get(id=advert_id)
        serializer = Listing_Serializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@swagger_auto_schema(method="PATCH", request_body=Listing_Serializer())
@api_view(["PATCH"])
def patch(request, advert_id):
    """Allows logged in users to edit the details of a job advert"""
    try:
        post = Listing.objects.get(id=advert_id)
    except Listing.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PATCH':
        # posting = Listing.objects.get(id=advert_id)
        serializer = Listing_Serializer(post, data=request.data, partial=True)
        data={}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method="DELETE")
@api_view(["DELETE"])
def delete(request, advert_id):
        """Delete a single job application"""
        try:
            posts = Listing.objects.get(id=advert_id)
        except Listing.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == "DELETE":
            serializer = posts.delete()
            data={}
            if serializer:
                data["success"] = "delete successful"
            else:
                data["failure"] = "delete failed"
            return Response(data=data)
            
           


# @swagger_auto_schema(method="patch", request_body=Listing_Serializer())
# @api_view(["patch"])
# def patch(request, advert_id):



class Posting(APIView):

    def get(self,requet, format=None):

        adverts = Listing.objects.all()

        return Response(adverts.values(), status=status.HTTP_200_OK )

    @swagger_auto_schema(method="post", request_body=Listing_Serializer())
    @action(methods=["post"], detail=True)
    def post(self, requet, format=None):

        serializer = Listing_Serializer(data=requet.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"success"}, status= status.HTTP_200_OK)
        
        return Response({"message":"falied", "error":serializer.errors}, status= status.HTTP_400_BAD_REQUEST)

    






