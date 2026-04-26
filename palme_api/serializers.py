# -*- coding: utf-8 -*-
"""
@File    : serializers.py
@Author  : Robusr
@Date    : 2026/4/27 02:40
@Description: 序列化器
@Software: PyCharm
"""
from rest_framework import serializers
from .models import Question, Option, Personality, Movie, UserSession, UserResult


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_text', 'order']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'scenario_image', 'order', 'options']


class PersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Personality
        fields = ['id', 'name', 'character_name', 'movie_name', 'character_image',
                  'core_traits', 'interpretation', 'suitable_genres']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'poster', 'genres', 'douban_rating',
                  'release_year', 'director', 'summary']


class UserResultSerializer(serializers.ModelSerializer):
    personality = PersonalitySerializer(read_only=True)
    movies = serializers.SerializerMethodField()

    class Meta:
        model = UserResult
        fields = ['id', 'personality', 'movies', 'created_at']

    def get_movies(self, obj):
        movie_ids = obj.recommended_movies
        movies = Movie.objects.filter(id__in=movie_ids)
        return MovieSerializer(movies, many=True).data


class SubmitAnswerRequestSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    question_id = serializers.IntegerField()
    option_id = serializers.IntegerField()


class SubmitAllAnswersRequestSerializer(serializers.Serializer):
    session_id = serializers.UUIDField()
    answers = serializers.ListField(
        child=serializers.DictField(
            child=serializers.IntegerField(),
            allow_empty=False
        ),
        min_length=7,
        max_length=7
    )
