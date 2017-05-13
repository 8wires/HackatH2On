from rest_framework import serializers
from dropchain import models

class HourSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Hour
        fields = ('value')

class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Day
        fields = ('value')

class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Month
        fields = ('value')

class TypeChallengeSerializer(serializers.ModelSerializer):
    hours = HourSerializer(many=True, read_only=True)

    class Meta:
        model = models.TypeChallenge
        fields = ('name', 'description','multiplier','obj','hours','days','months')

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Challenge
        fields = ('typechallenge', 'goal')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('name','description','location','goal')

class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Priority
        fields = ('value','project','user')

class DropUserSerializer(serializers.ModelSerializer):
    challenges = ChallengeSerializer(many=True, read_only=True)

    class Meta:
        model = models.DropUser
        fields = ('user', 'challenges', 'priorities')
