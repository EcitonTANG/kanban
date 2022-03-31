from rest_framework import serializers
from .models import *


class Executor_TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor_Tab
        fields = ('first_name', 'last_name', 'second_name')
        
class Card_TabSerializer(serializers.ModelSerializer):
    fio = Executor_TabSerializer(many=True)
    
    class Meta:
        model = Card_Tab
        fields = ("card_id", "fio", "title", "description", "card_date")
        
        
class Column_TabSerializer(serializers.ModelSerializer):
    cards = Card_TabSerializer(many=True)
    
    class Meta:
        model = Column_Tab
        fields = ('column_id', 'column_name', 'cards')