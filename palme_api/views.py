# -*- coding: utf-8 -*-
"""
@File    : views.py
@Author  : Robusr
@Date    : 2026/4/27 02:45
@Description: api视图配置
@Software: PyCharm
"""
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Question, Option, Personality, Movie, UserSession, UserAnswer, UserResult
from .serializers import (
    QuestionSerializer, PersonalitySerializer, MovieSerializer,
    UserResultSerializer, SubmitAnswerRequestSerializer,
    SubmitAllAnswersRequestSerializer
)
from .services.personality_service import PersonalityService


# 移除这行：from .services.recommendation_service import recommendation_service

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all().order_by('order')
    serializer_class = QuestionSerializer


class PersonalityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Personality.objects.all()
    serializer_class = PersonalitySerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SessionViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def create_session(self, request):
        session = UserSession.objects.create()
        return Response({'session_id': session.id}, status=status.HTTP_201_CREATED)


class AnswerViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def submit_answer(self, request):
        serializer = SubmitAnswerRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        session_id = serializer.validated_data['session_id']
        question_id = serializer.validated_data['question_id']
        option_id = serializer.validated_data['option_id']

        try:
            session = UserSession.objects.get(id=session_id)
            question = Question.objects.get(id=question_id)
            option = Option.objects.get(id=option_id, question=question)
        except (UserSession.DoesNotExist, Question.DoesNotExist, Option.DoesNotExist):
            return Response({'error': '无效的会话、问题或选项'}, status=status.HTTP_404_NOT_FOUND)

        UserAnswer.objects.update_or_create(
            session=session,
            question=question,
            defaults={'selected_option': option}
        )

        return Response({'status': 'success'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def submit_all_answers(self, request):
        # 在函数内部导入，避免模块级导入
        from .services.recommendation_service import recommendation_service

        serializer = SubmitAllAnswersRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        session_id = serializer.validated_data['session_id']
        answers_data = serializer.validated_data['answers']

        try:
            session = UserSession.objects.get(id=session_id)
        except UserSession.DoesNotExist:
            return Response({'error': '无效的会话'}, status=status.HTTP_404_NOT_FOUND)

        user_answers = []
        for answer_data in answers_data:
            question_id = answer_data['question_id']
            option_id = answer_data['option_id']

            try:
                question = Question.objects.get(id=question_id)
                option = Option.objects.get(id=option_id, question=question)
            except (Question.DoesNotExist, Option.DoesNotExist):
                return Response({'error': f'无效的问题或选项: {question_id}'}, status=status.HTTP_404_NOT_FOUND)

            user_answer, _ = UserAnswer.objects.update_or_create(
                session=session,
                question=question,
                defaults={'selected_option': option}
            )
            user_answers.append(user_answer)

        user_preference = PersonalityService.calculate_user_preference(user_answers)
        personality = PersonalityService.match_personality(user_preference)
        recommended_movie_ids = recommendation_service.recommend_movies(user_preference)

        user_result = UserResult.objects.create(
            session=session,
            personality=personality,
            preference_vector=user_preference,
            recommended_movies=recommended_movie_ids
        )

        result_serializer = UserResultSerializer(user_result)
        return Response(result_serializer.data, status=status.HTTP_200_OK)


class ResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserResult.objects.all()
    serializer_class = UserResultSerializer

    @action(detail=False, methods=['get'])
    def get_by_session(self, request):
        session_id = request.query_params.get('session_id')
        if not session_id:
            return Response({'error': '缺少session_id参数'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            result = UserResult.objects.get(session__id=session_id)
            serializer = UserResultSerializer(result)
            return Response(serializer.data)
        except UserResult.DoesNotExist:
            return Response({'error': '结果不存在'}, status=status.HTTP_404_NOT_FOUND)