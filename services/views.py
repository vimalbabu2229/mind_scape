from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Goal
from .serializers import GoalSerializer

class GoalViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

