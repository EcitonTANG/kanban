from django.db import models

# Create your models here.
class Executor_Tab(models.Model):
    executor_id = models.IntegerField(primary_key=True);
    first_name = models.CharField(max_length=128);
    last_name = models.CharField(max_length=128);
    second_name = models.CharField(max_length=128);
    
    def __str__(self):
        return self.executor_id
    
class Column_Tab(models.Model):
    column_id = models.IntegerField(primary_key=True);
    column_name = models.CharField(max_length=128);
    cards = models.ManyToManyField('Card_Tab', verbose_name="card_tab", related_name="card_tab_name");
    
    def __str__(self):
        return self.column_id

class Card_Tab(models.Model):
    card_id = models.IntegerField(primary_key=True);
    title = models.CharField(max_length=256);
    description = models.TextField();
    card_date = models.DateField();
    executor_id = models.ForeignKey(Executor_Tab, on_delete=models.CASCADE);
    column_id = models.ForeignKey(Column_Tab, on_delete=models.CASCADE);
    
    def __str__(self):
        return self.card_id