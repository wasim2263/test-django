from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ("Date information", {'fields': ['pub_date']}),
    ]
    # inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

