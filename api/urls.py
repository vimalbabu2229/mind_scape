from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.views import AccountsViewSet

router: DefaultRouter = DefaultRouter()
# ____________________ ACCOUNTS APIs ________________________
router.register(r"accounts", AccountsViewSet, basename="accounts")
"""
End Points:

    POST    /api/accounts/register/     ==> register user with username, email, password
    POST    /api/accounts/login/        ==> login user with username and password
    POST    /api/accounts/logout/       ==> logout authenticated users
    DELETE  /api/accounts/delete/       ==> delete authenticated user account
    GET     /api/accounts/profile/      ==> get complete profile details
    PATCH   /api/accounts/profile/      ==> update profile details. Username and email cannot 
                                            be changed 
"""

# Url patterns 
urlpatterns = [
    path('', include(router.urls)),
]
