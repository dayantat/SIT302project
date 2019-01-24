from django.contrib import admin
from .models import Question, Choice, Category

# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question", {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ("Category", {'fields': ['category_text']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'category_text')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# class CategoryAdmin(admin.ModelAdmin):
#

admin.site.register(Question, QuestionAdmin)


