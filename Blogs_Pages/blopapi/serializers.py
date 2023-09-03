from rest_framework import serializers
from Blogs.models import BlogPost
from django.contrib.auth.models import User

class BlogSerializer(serializers.ModelSerializer):
  class Meta:
    fields=["title","slug","content"]
    model=BlogPost

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    fields=["firstname","lastname","username"]
    model=User