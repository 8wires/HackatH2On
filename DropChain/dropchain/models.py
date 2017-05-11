from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

class Hour(models.Model):
    """Instance of an hour. There will be at most one per hour a day has."""
    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 24

    @classmethod
    def create(cls, value):
        hour = cls(value = value)
        return hour

#class HourChallenge(Challenge):
#    hours = models.ManyToManyField(Hour)

class Day(models.Model):
    """Instance of a day. There will be at most one per day a week has."""

    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 7

    @classmethod
    def create(cls, value):
        day = cls(value = value)
        return day

#class DayChallenge(Challenge):
#    days = models.ManyToManyField(Day)

class Month(models.Model):
    """Instance of a month. There will be at most one per month a year has."""
    value = models.PositiveSmallIntegerField(primary_key=True) # From 1 to 12

    @classmethod
    def create(cls, value):
        month = cls(value = value)
        return month

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

    @classmethod
    def create(cls, name, description, multiplier, goal, hours, days, months):
        challenge = cls(name = name, description = description, multiplier = multiplier, goal = goal, hours = hours, days = days, months = months)
        return challenge

class Project(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.CharField(max_length=1000)
    location = models.CharField(max_length=100) # Neighbourhood, city or other (no specific format)
    goal = models.PositiveIntegerField()

    @classmethod
    def create(cls, name, description, location, goal):
        project = cls(name = name, description = description, location = location, goal = goal)
        return project

class Priority(models.Model):
    class Meta:
        unique_together = (('value', 'user'),('user','project'),)
    
    PRIORITIES_VALUES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
    )

    value = models.CharField(max_length=1, choices=PRIORITIES_VALUES)
    #value = PositiveSmallIntegerField() # From 1 (highest priority) to 3 (lowest)
    project = models.OneToOneField(Project)
    user = models.OneToOneField(User)

    @classmethod
    def create(cls, value, project, user):
        priority = cls(value = value, project = project , user = user)
        return priority

class DropUser(models.Model):
    """User of our system. The username corresponds to the contract number,
    the first_name to the name the user wants to be seen as."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    challenges = models.ManyToManyField(Challenge)
    priorities = models.ForeignKey(Priority)

    @classmethod
    def create(cls, user, challenges, priorities):
        dropuser = cls(user = user, challenges = challenges, priorities = priorities)
        return dropuser

