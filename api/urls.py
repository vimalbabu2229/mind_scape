from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.views import AccountsViewSet

router: DefaultRouter = DefaultRouter()
# ____________________ ACCOUNTS APIs ________________________
router.register(r"accounts", AccountsViewSet, basename="accounts")

# Url patterns 
urlpatterns = [
    path('', include(router.urls)),
]
