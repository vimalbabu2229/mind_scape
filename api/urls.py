from rest_framework.routers import DefaultRouter
from django.urls import path, include

router: DefaultRouter = DefaultRouter()

# router.register(r"uploads", UploadsViewSet, basename="uploads")

# Url patterns 
urlpatterns = [
    path('', include(router.urls)),
]
