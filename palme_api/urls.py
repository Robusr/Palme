# -*- coding: utf-8 -*-
"""
@File    : urls.py
@Author  : Robusr
@Date    : 2026/4/27 02:44
@Description: api应用路由配置
@Software: PyCharm
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    QuestionViewSet, PersonalityViewSet, MovieViewSet,
    SessionViewSet, AnswerViewSet, ResultViewSet
)

router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'personalities', PersonalityViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'sessions', SessionViewSet, basename='session')
router.register(r'answers', AnswerViewSet, basename='answer')
router.register(r'results', ResultViewSet, basename='result')

urlpatterns = [
    path('', include(router.urls)),
]
