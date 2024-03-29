from .models import Theme, Question, Author, Answer
from rest_framework import viewsets, permissions
from .serializers import ThemeSerializer, QuestionSerializer, AuthorSerializer, AnswerSerializer


class ThemeViewSet(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ThemeSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = QuestionSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AuthorSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AnswerSerializer
