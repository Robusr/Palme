# -*- coding: utf-8 -*-
"""
@File    : models.py
@Author  : Robusr
@Date    : 2026/4/27 02:39
@Description: 数据库模型
@Software: PyCharm
"""
from django.db import models
import uuid


class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.TextField(verbose_name="问题内容")
    scenario_image = models.CharField(max_length=255, verbose_name="情景图片路径")
    order = models.IntegerField(verbose_name="题目顺序", unique=True)

    class Meta:
        ordering = ['order']
        verbose_name = "问题"
        verbose_name_plural = "问题"

    def __str__(self):
        return f"第{self.order}题: {self.question_text[:30]}"


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=255, verbose_name="选项内容")
    preference_vector = models.JSONField(verbose_name="电影偏好向量")
    order = models.IntegerField(verbose_name="选项顺序")

    class Meta:
        ordering = ['order']
        verbose_name = "选项"
        verbose_name_plural = "选项"

    def __str__(self):
        return f"{self.option_text[:30]}"


class Personality(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="人格类型名称")
    character_name = models.CharField(max_length=100, verbose_name="对应电影角色名")
    movie_name = models.CharField(max_length=100, verbose_name="出自电影")
    character_image = models.CharField(max_length=255, verbose_name="角色图片路径")
    core_traits = models.TextField(verbose_name="核心特质")
    interpretation = models.TextField(verbose_name="人格解读")
    suitable_genres = models.CharField(max_length=255, verbose_name="最适配电影风格")
    match_threshold = models.JSONField(verbose_name="匹配阈值向量")

    class Meta:
        verbose_name = "人格画像"
        verbose_name_plural = "人格画像"

    def __str__(self):
        return f"{self.name} - {self.character_name}"


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name="电影名称")
    poster = models.CharField(max_length=255, verbose_name="海报路径")
    genres = models.CharField(max_length=255, verbose_name="类型")
    douban_rating = models.FloatField(verbose_name="豆瓣评分")
    release_year = models.IntegerField(verbose_name="上映年份")
    director = models.CharField(max_length=100, verbose_name="导演")
    summary = models.TextField(verbose_name="简介")
    feature_vector = models.JSONField(verbose_name="电影特征向量")

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = "电影"

    def __str__(self):
        return f"{self.title} ({self.release_year})"


class UserSession(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "用户会话"
        verbose_name_plural = "用户会话"

    def __str__(self):
        return str(self.id)


class UserAnswer(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.ForeignKey(UserSession, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE)
    answered_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'question')
        verbose_name = "用户答题记录"
        verbose_name_plural = "用户答题记录"

    def __str__(self):
        return f"{self.session.id} - 第{self.question.order}题"


class UserResult(models.Model):
    id = models.AutoField(primary_key=True)
    session = models.OneToOneField(UserSession, on_delete=models.CASCADE, related_name='result')
    personality = models.ForeignKey(Personality, on_delete=models.CASCADE)
    preference_vector = models.JSONField(verbose_name="用户偏好向量")
    recommended_movies = models.JSONField(verbose_name="推荐电影ID列表")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "用户结果"
        verbose_name_plural = "用户结果"

    def __str__(self):
        return f"{self.session.id} - {self.personality.name}"