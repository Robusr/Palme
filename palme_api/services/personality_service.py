# -*- coding: utf-8 -*-
"""
@File    : personality_service.py
@Author  : Robusr
@Date    : 2026/4/27 02:42
@Description: 电影人格匹配服务
@Software: PyCharm
"""
import numpy as np
from palme_api.models import Personality


class PersonalityService:
    @staticmethod
    def calculate_user_preference(answers):
        """
        根据用户答题结果计算7维偏好向量
        answers: 包含selected_option对象的列表
        """
        preference_vectors = []
        for answer in answers:
            vector = np.array(answer.selected_option.preference_vector)
            preference_vectors.append(vector)

        # 计算平均偏好向量
        user_preference = np.mean(preference_vectors, axis=0)
        return user_preference.tolist()

    @staticmethod
    def match_personality(user_preference):
        """
        根据用户偏好向量匹配最适合的人格类型
        """
        personalities = Personality.objects.all()
        best_match = None
        min_distance = float('inf')

        user_vector = np.array(user_preference)

        for personality in personalities:
            threshold_vector = np.array(personality.match_threshold)
            # 计算欧氏距离
            distance = np.linalg.norm(user_vector - threshold_vector)

            if distance < min_distance:
                min_distance = distance
                best_match = personality

        return best_match