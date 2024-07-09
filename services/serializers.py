from rest_framework import serializers 
from .models import Goal, Journal, JournalImages

import json

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"
        read_only_fields = ['user']

class JournalImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalImages
        fields = ['id', 'image']


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ['id','date', 'thoughts', 'doodle', 'audio']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        images = JournalImages.objects.filter(journal=instance.id)
        representation['images'] = JournalImagesSerializer(images, many=True, context=self.context).data
        return representation