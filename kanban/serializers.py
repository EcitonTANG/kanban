from rest_framework import serializers
from .models import *


class Executor_TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Executor_Tab
        fields = ('executor_id', 'first_name', 'last_name', 'second_name')
        
class Card_TabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card_Tab
        fields = '__all__'


class Card_TabForColumnSerializer(serializers.ModelSerializer):
    #fio = Executor_TabSerializer(many=True)
    class Meta:
        model = Card_Tab
        fields = ("card_id", "executor_id", "title", "description", "card_date")

        
class Column_TabDetailSerializer(serializers.ModelSerializer):
    cards = Card_TabForColumnSerializer(many=True)

    class Meta:
        model = Column_Tab
        fields = ('column_id', 'column_name', 'cards')

class Column_TabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column_Tab
        fields = ('column_id', 'column_name')