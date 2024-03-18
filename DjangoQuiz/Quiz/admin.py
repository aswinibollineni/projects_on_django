from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'option1', 'option2', 'option3', 'option4', 'correct_answer')
    search_fields = ['question_text', 'correct_answer']

# Register your models here.
admin.site.register(Question, QuestionAdmin)


