from django.http import Http404
from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.
class Executor_TabAPIView(APIView):
    def get_object(self, pk):
        try:
            return Executor_Tab.objects.get(pk=pk)
        except Executor_Tab.DoesNotExist:
            raise Http404

    def get(self, request):
        executors = Executor_Tab.objects.all()
        serializer = Executor_TabSerializer(executors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Executor_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        executor = self.get_object(pk)
        executor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
class Column_TabAPIView(APIView):
    def get_object(self, pk):
        try:
            return Column_Tab.objects.get(pk=pk)
        except Column_Tab.DoesNotExist:
            raise Http404

    def get(self, request):
        columns = Column_Tab.objects.all()
        serializer = Column_TabDetailSerializer(columns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Column_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        column = self.get_object(pk)
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Card_TabAPIView(APIView):
    def get_object(self, pk):
        try:
            return Card_Tab.objects.get(pk=pk)
        except Card_Tab.DoesNotExist:
            raise Http404

    def get(self, request):
        cards = Card_Tab.objects.all()
        serializer = Card_TabSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Card_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        card = self.get_object(pk)
        card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)