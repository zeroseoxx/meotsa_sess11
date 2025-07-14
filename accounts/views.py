# accounts/views.py
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
# accounts/views.py

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CustomUserDetailSerializer

@api_view(['GET'])
@permission_classes([IsAuthenticated])  # 로그인한 사용자만 접근 가능
def user_detail(request):
    user = request.user
    serializer = CustomUserDetailSerializer(user)
    return Response(serializer.data)
