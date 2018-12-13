from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.


admin.register(Question)(admin.ModelAdmin)
admin.register(Choice)(admin.ModelAdmin)
