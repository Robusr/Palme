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


# 定义简单的DQN网络
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
    def __init__(self):
        self.movies = list(Movie.objects.all())
        self.movie_vectors = np.array([movie.feature_vector for movie in self.movies])
        self.state_dim = 7  # 7维偏好向量
        self.action_dim = len(self.movies)

        # 初始化DQN模型
        self.model = DQN(self.state_dim, self.action_dim)
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.criterion = nn.MSELoss()

    def recommend_movies(self, user_preference, num_recommendations=8):
        """
        使用DQN模型推荐电影
        user_preference: 7维用户偏好向量
        num_recommendations: 推荐电影数量
        """
        state = torch.FloatTensor(user_preference).unsqueeze(0)

        # 前向传播获取Q值
        with torch.no_grad():
            q_values = self.model(state)

        # 获取Q值最高的电影索引
        _, top_indices = torch.topk(q_values, num_recommendations)
        top_indices = top_indices.squeeze().tolist()

        # 返回推荐的电影ID
        recommended_movie_ids = [self.movies[i].id for i in top_indices]
        return recommended_movie_ids

    def train_model(self, user_preference, selected_movie_id, reward=1.0):
        """
        训练模型（当用户点击推荐电影时调用）
        """
        state = torch.FloatTensor(user_preference).unsqueeze(0)
        action = self.movies.index(Movie.objects.get(id=selected_movie_id))

        # 计算目标Q值
        current_q = self.model(state)
        target_q = current_q.clone()
        target_q[0, action] = reward

        # 反向传播
        self.optimizer.zero_grad()
        loss = self.criterion(current_q, target_q)
        loss.backward()
        self.optimizer.step()

        return loss.item()


# 全局推荐服务实例
recommendation_service = RecommendationService()
