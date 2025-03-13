from django.contrib import admin
from .models import ContactMessage



@admin.register(ContactMessage)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')