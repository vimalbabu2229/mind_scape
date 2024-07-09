from django.db import models
from  accounts.models import User

# ++++++++++++++++++ GOAL MODEL +++++++++++++++++++++
class Goal(models.Model):
    date = models.DateField()
    category = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.category
    
# +++++++++++++++++++++ JOURNAL MODEL ++++++++++++++++++++++
class Journal(models.Model):
    created_on = models.DateField(auto_now_add=True, unique=True)
    thoughts = models.TextField()
    # Storing doodle as json
    doodle = models.JSONField(null=True)
    audio = models.FileField(upload_to="audio/", null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.id} - {self.created_on}"

# +++++++++++++++++++ JOURNAL IMAGES MODEL +++++++++++++++++++
class JournalImages(models.Model):
    """
    Since a journal can have multiple images , we are keeping a separate
    page to hold the images related to each journal 
    """
    image = models.ImageField(upload_to="images/")
    journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.journal)