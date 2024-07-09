from django.contrib import admin
from .models import Goal, Journal, JournalImages

admin.site.register(Goal)
admin.site.register(Journal)
admin.site.register(JournalImages)