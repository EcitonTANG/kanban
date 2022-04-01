from rest_framework import generics, status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.
class Executor_TabAPIView(APIView):
    def get(self, request):
        executors = Executor_Tab.objects.all()
        serializer = Executor_TabSerializer(executors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Column_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #queryset = Executor_Tab.objects.all()
    #serializer_class = Executor_TabSerializer
            
class Column_TabAPIView(APIView):
    def get(self, request):
        columns = Column_Tab.objects.all()
        serializer = Column_TabSerializer(columns, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Column_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    ''' 
        data = {
            '': request.data.get(''),
        }
        serializer = Column_TabSerializer(data=data)
            if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    '''
    
class Card_TabAPIView(APIView):
    def get(self, request):
        cards = Card_Tab.objects.all()
        serializer = Card_TabSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Column_TabSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #queryset = Card_Tab.objects.all()
    #serializer_class = Card_TabSerializer