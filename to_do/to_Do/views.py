import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, views, status

import to_Do.models
from to_Do.serializers import ToDoItemDetailSerializer, ToDoItemListSerializer
from to_Do.models import ToDoItem, User
from to_Do.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class Logout(views.APIView):

    def get(self, request, format=None):
        request.user.auth_token.delete()

        return Response(status=status.HTTP_200_OK)


class ToDoCreateView(generics.CreateAPIView):
    serializer_class = ToDoItemDetailSerializer


class ToDoListView(generics.ListAPIView):
    def get(self, request):
        user = request.user
        print(user.id)
        queryset = ToDoItem.objects.filter(user_id=user.id).values()
        return Response(data=queryset)

    serializer_class = ToDoItemListSerializer
    permission_classes = (IsAuthenticated, )

class ToDoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ToDoItemDetailSerializer
    queryset = ToDoItem.objects.all()
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticated)