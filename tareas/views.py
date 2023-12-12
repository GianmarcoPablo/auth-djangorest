# from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import TaskSerializer, UserSerializer
from .models import Task
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes


@api_view(['POST'])
def login(request):
    username = get_object_or_404(User, username=request.data['username'])
    if not username.check_password(request.data['password']):
        return Response({"error": "Contraseña incorrecta"}, status=status.HTTP_400_BAD_REQUEST)
    token = Token.objects.get(user=username)
    serializer = UserSerializer(instance=username)
    return Response({"token": token.key,"user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key,"user": serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([
    SessionAuthentication,
    TokenAuthentication,
])
@permission_classes([IsAuthenticated])
def test_token(request):
    #BEARER TOKEN
    print(request.user)
    return Response("passed for {}".format(request.user.email))