from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Question(models.Model):
    CATEGORY_CHOICES = (
        ('Science', 'Science'),
        ('Arts', 'Arts'),
        ('Commerce', 'Commerce')
    )
    question = models.CharField(max_length=1000, default="", null=False)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    date_added = models.DateField(default=timezone.now)

    def __str__(self):
        return self.question


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_label = models.CharField(max_length=1000)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_label


class TestHistory(models.Model):
    user = models.ForeignKey(User)
    test_date = models.DateField(default=timezone.now)
    science_score = models.IntegerField()
    arts_score = models.IntegerField()
    commerce_score = models.IntegerField()
