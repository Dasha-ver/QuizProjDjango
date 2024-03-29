from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Theme(models.Model):
    title = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    phone_number = PhoneNumberField(unique=True, null=True)
    user_email = models.EmailField(max_length=70, unique=True, null=True)
    password = models.CharField(max_length=12, unique=True, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question_text']
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f' {self.question_text}/{self.theme}/{self.author}'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_text = models.CharField(max_length=200)
    correct_answer = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['question']
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return f'{self.question}/{self.answer_text}/{self.correct_answer}'
