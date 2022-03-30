from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.
class Executor_TabAPIView(generics.ListAPIView):
    queryset = Executor_Tab.objects.all()
    serializer_class = Executor_TabSerializer
            
class Column_TabAPIView(APIView):
    def get(self, request):
        columns = Column_Tab.objects.filter()
        serializer = Column_TabSerializer(columns, many=True)
        return Response(serializer.data)
    
class Card_TabAPIView(generics.ListAPIView):
    queryset = Card_Tab.objects.all()
    serializer_class = Card_TabSerializer