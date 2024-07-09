from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django.db import IntegrityError

from .models import Goal, JournalImages, Journal
from .serializers import GoalSerializer, JournalSerializer

class GoalViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = GoalSerializer

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class JournalViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = JournalSerializer(data=request.data, context={'request': request} )
        try :
            if serializer.is_valid():
                journal = serializer.save(user = request.user)
                images = request.FILES.getlist('images')
                if images :
                    for image in images:
                        JournalImages.objects.create(journal=journal, image= image)
                
                return Response(JournalSerializer(journal, context={'request': request} ).data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError as e :
            return Response({'detail': 'Journal already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as e :
            return Response({'detail': f'Something went wrong ({str(e)})'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        if not 'date' in request.data:
            return Response({'detail': 'Specify the date to retrieve your journal'}, status=status.HTTP_400_BAD_REQUEST)
        
        date = request.data['date']
        journal = Journal.objects.filter(created_on=date)
        if not journal.exists():
            return Response({}, status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = JournalSerializer(journal[0], context={'request':request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    def update(self, request, pk=None):
        try :
            instance = Journal.objects.get(pk=pk)
            serializer = JournalSerializer(instance, data=request.data, context={'request': request})
            if serializer.is_valid():
                journal = serializer.save(user=request.user)
                return Response(JournalSerializer(journal, context={'request': request} ).data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        except Journal.DoesNotExist:
            return Response({'detail': 'Journal does not exist'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e :
            return Response({'detail': 'Something went wrong'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)