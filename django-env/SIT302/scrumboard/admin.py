from django.contrib import admin
from .models import List, Card
# Register your models here.

admin.site.register(List)  # This allows for the link to be accessible in the admin page
admin.site.register(Card)  # This allows for the link to be accessible in the admin page
