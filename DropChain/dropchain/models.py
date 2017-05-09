from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Hour(models.Model):
    """Instance of an hour. There will be at most one per hour a day has."""
    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 24

#class HourChallenge(Challenge):
#    hours = models.ManyToManyField(Hour)

class Day(models.Model):
    """Instance of a day. There will be at most one per day a week has."""
    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 7

#class DayChallenge(Challenge):
#    days = models.ManyToManyField(Day)

class Month(models.Model):
    """Instance of a month. There will be at most one per month a year has."""
    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 12

#class MonthChallenge(Challenge):
#    months = models.ManyToManyField(Month)

class Challenge(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=1000)
    multiplier = models.PositiveSmallIntegerField(default=1) # Reward multiplier
    goal = models.PositiveSmallIntegerField()   # Is it a percentage??? (0 to 1)
    hours = models.ManyToManyField(Hour)
    days = models.ManyToManyField(Day)
    months = models.ManyToManyField(Month)

class Project(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100) # Neighbourhood, city or other (no specific format)
    goal = models.PositiveIntegerField()

class Priority(models.Model):
    PRIORITIES_VALUES = (
        ('1', '1'),
        ('3', '2'),
        ('3', '3'),
    )
    value = models.CharField(max_length=1, choices=PRIORITIES_VALUES)
    #value = PositiveSmallIntegerField() # From 1 (highest priority) to 3 (lowest)
    project = models.ManyToManyField(Project)

class DropUser(User):
    """User of our system. The username corresponds to the contract number,
    the first_name to the name the user wants to be seen as."""
    challenges = models.ManyToManyField(Challenge)
    priorities = models.ForeignKey(Priority)
    #priority1 = models.ForeignKey(Project, on_delete=models.CASCADE)
    #priority2 = models.ForeignKey(Project, on_delete=models.CASCADE)
    #priority3 = models.ForeignKey(Project, on_delete=models.CASCADE)
