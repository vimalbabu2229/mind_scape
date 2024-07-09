from django.contrib import admin
from .models import Goal, Journal, JournalImages

class GoalAdmin(admin.ModelAdmin):
    list_display = ('date', 'category', 'user', 'created_at')

class JournalAdmin(admin.ModelAdmin):
    list_display = ('date', 'user', 'thoughts')

class JournalImagesAdmin(admin.ModelAdmin):
    list_display = ('journal', 'image')

# Register models
admin.site.register(Goal, GoalAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(JournalImages, JournalImagesAdmin)