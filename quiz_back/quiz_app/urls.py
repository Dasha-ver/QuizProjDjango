from rest_framework import routers
from .api import ThemeViewSet, QuestionViewSet, AuthorViewSet, AnswerViewSet


router = routers.DefaultRouter()
router.register('themes', ThemeViewSet)
router.register('questions', QuestionViewSet)
router.register('authors', AuthorViewSet)
router.register('answers', AnswerViewSet)
urlpatterns = router.urls