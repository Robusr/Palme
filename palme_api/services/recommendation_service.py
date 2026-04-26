# -*- coding: utf-8 -*-
"""
@File    : recommendation_service.py
@Author  : Robusr
@Date    : 2026/4/27 02:43
@Description: 强化学习推荐服务
@Software: PyCharm
"""

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from palme_api.models import Movie


class DQN(nn.Module):
    def __init__(self, state_dim, action_dim):
        super(DQN, self).__init__()
        self.fc1 = nn.Linear(state_dim, 64)
        self.fc2 = nn.Linear(64, 32)
        self.fc3 = nn.Linear(32, action_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)


class RecommendationService:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not self._initialized:
            self._initialized = True
            # 不在 __init__ 中加载数据，改为懒加载
            self.movies = None
            self.movie_vectors = None
            self.model = None
            self.optimizer = None
            self.criterion = None
            self.state_dim = 7

    def _initialize(self):
        """懒加载初始化：在第一次使用时才加载数据"""
        if self.movies is None:
            self.movies = list(Movie.objects.all())
            self.movie_vectors = np.array([movie.feature_vector for movie in self.movies])
            self.action_dim = len(self.movies)

            self.model = DQN(self.state_dim, self.action_dim)
            self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
            self.criterion = nn.MSELoss()

    def recommend_movies(self, user_preference, num_recommendations=8):
        self._initialize()  # 确保已初始化

        state = torch.FloatTensor(user_preference).unsqueeze(0)

        with torch.no_grad():
            q_values = self.model(state)

        _, top_indices = torch.topk(q_values, num_recommendations)
        top_indices = top_indices.squeeze().tolist()

        recommended_movie_ids = [self.movies[i].id for i in top_indices]
        return recommended_movie_ids

    def train_model(self, user_preference, selected_movie_id, reward=1.0):
        self._initialize()  # 确保已初始化

        state = torch.FloatTensor(user_preference).unsqueeze(0)
        action = self.movies.index(Movie.objects.get(id=selected_movie_id))

        current_q = self.model(state)
        target_q = current_q.clone()
        target_q[0, action] = reward

        self.optimizer.zero_grad()
        loss = self.criterion(current_q, target_q)
        loss.backward()
        self.optimizer.step()

        return loss.item()


# 全局实例，但此时不会初始化数据库访问
recommendation_service = RecommendationService()