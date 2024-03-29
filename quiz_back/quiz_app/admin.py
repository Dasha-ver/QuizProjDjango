from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
from .models import Question, Author, Answer, Theme


class AnswerAdmin(admin.ModelAdmin):
    list_display = 'id', 'question', 'answer_text', 'correct_answer', 'date'
    list_filter = 'id', 'question', 'date'


class AnswerInline(NestedStackedInline):
    fields = 'question', 'answer_text', 'correct_answer',
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = 'id', 'question_text', 'theme', 'author', 'date'
    list_filter = 'id', 'author', 'theme', 'question_text', 'date'


class QuestionInline(NestedStackedInline):
    inlines = [AnswerInline]
    model = Question
    fields = 'question_text', 'theme', 'author',
    extra = 1


class AuthorAdmin(NestedModelAdmin):
    inlines = [QuestionInline]
    fields = 'name', 'phone_number', 'user_email', 'password'
    list_display = 'id', 'name', 'phone_number', 'user_email', 'password', 'date'
    list_filter = 'id', 'name', 'date'


class ThemeAdmin(admin.ModelAdmin):
    fields = 'title',
    list_display = 'id', 'title',
    list_filter = 'id', 'title', 'date'


admin.site.register(Theme, ThemeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Answer, AnswerAdmin)
