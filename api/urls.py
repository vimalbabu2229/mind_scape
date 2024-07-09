from rest_framework.routers import DefaultRouter
from django.urls import path, include
from accounts.views import AccountsViewSet
from services.views import GoalViewSet, JournalViewSet, JournalImageViewSet

router: DefaultRouter = DefaultRouter()
# ____________________ ACCOUNTS APIs ________________________
# Accounts application manages user authentication services 
router.register(r"accounts", AccountsViewSet, basename="accounts")
"""
End Points:

    POST    /api/accounts/register/     ==> register user with 'username', 'email', 'password'
    POST    /api/accounts/login/        ==> login user with 'username' and 'password'
    POST    /api/accounts/logout/       ==> logout authenticated users
    DELETE  /api/accounts/delete/       ==> delete authenticated user account
    GET     /api/accounts/profile/      ==> get complete profile details
    PATCH   /api/accounts/profile/      ==> update profile details - 'username' and 'email' cannot 
                                            be changed 
"""

# _________________________ SERVICES APIs ____________________________
# Services application provides functionalities such as goal and journal

# ++++++++ goal apis +++++++++++   
router.register(r"services/goal", GoalViewSet, basename="services_goal")
"""
Endpoints:
    POST    /api/services/goal/         ==> create a new goal providing 'date' in YYY-MM-DD format,  
                                            'category', and   'description' .
    GET     /api/services/goal/         ==> get all the goals of the user
    PATCH   /api/services/goal/<id>/    ==> update the goal with provided 'id'
    DELETE  /api/services/goal/<id>/    ==> goal with the provided 'id' will be deleted 
"""   
# ++++++++ journal apis ++++++++++                    
router.register(r"services/journal", JournalViewSet, basename="services_journal")
"""
Endpoints:
    POST    /api/services/journal/      ==> crate a new journal providing required fields
    GET     /api/services/journal/      ==> provide a 'date' to get the journal details
    PUT     /api/services/journal/<id>/ ==> update journal details
"""
# ++++++++ journal image apis ++++++++
router.register(r"services/journal/images", JournalImageViewSet, basename="services_journal_images")
"""
Endpoints:
    POST    /api/services/journal/images/<journal_id>/add/      ==> add new image to the journal
                                                                    passing 'image' and journal id 
    DELETE  /api/services/journal/images/<image_id>/delete/     ==> delete an image passing 
                                                                    image id 
"""
# Url patterns 
urlpatterns = [
    path('', include(router.urls)),
]
