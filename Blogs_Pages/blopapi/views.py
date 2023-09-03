from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework .views import APIView
from  blopapi.serializers import BlogSerializer
from Blogs.models import BlogPost
from django.contrib.auth.models import User
# Create your views here.

class BlogApiView(APIView):
    def get(self,request):
        blg_obj = BlogPost.objects.all()
        serializer = BlogSerializer(blg_obj,many=True)
        return Response(serializer.data)
    
    def post (self,request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)   
