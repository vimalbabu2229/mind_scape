from rest_framework import serializers 
from .models import Goal, Journal, JournalImages

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ['user']

# class JournalSerializer()