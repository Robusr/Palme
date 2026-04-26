# -*- coding: utf-8 -*-
"""
@File    : admin.py
@Author  : Robusr
@Date    : 2026/4/27 02:37
@Description: 管理员应用
@Software: PyCharm
"""
from django.contrib import admin
from .models import Question, Option, Personality, Movie, UserSession, UserAnswer, UserResult  # 修改这里


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'order')
    search_fields = ('question_text',)


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'option_text', 'order')
    list_filter = ('question',)
    search_fields = ('option_text',)


@admin.register(Personality)
class PersonalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'character_name', 'movie_name')
    search_fields = ('name', 'character_name', 'movie_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genres', 'douban_rating', 'release_year', 'director')
    list_filter = ('genres', 'release_year')
    search_fields = ('title', 'director', 'summary')


@admin.register(UserSession)
class UserSessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(UserAnswer)
class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'question', 'selected_option', 'answered_at')
    readonly_fields = ('answered_at',)


@admin.register(UserResult)
class UserResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'session', 'personality', 'created_at')
    readonly_fields = ('preference_vector', 'recommended_movies', 'created_at')
