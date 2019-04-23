from django.db import models
import time
from datetime import *
# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class Word(models.Model):
    no = models.ForeignKey('User', on_delete=models.CASCADE)
    word = models.CharField(max_length=50)
    count = models.IntegerField()
    word_part = models.CharField(max_length=30)
    datetime = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.word



class Emotion(models.Model):
    no = models.ForeignKey('User', on_delete=models.CASCADE)
    sentence = models.TextField()
    negative = models.FloatField()
    neutral = models.FloatField()
    positive = models.FloatField()
    datetime = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.sentence