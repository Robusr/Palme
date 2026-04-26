# -*- coding: utf-8 -*-
"""
@File    : initial_data.py
@Author  : Robusr
@Date    : 2026/4/27 02:48
@Description: 初始数据填充脚本
@Software: PyCharm
"""

import os
import django
import json

# 设置Django环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Palme.settings')
django.setup()

from palme_api.models import Question, Option, Personality, Movie


def populate_questions_and_options():
    """填充问题和选项数据"""
    print("正在填充问题和选项数据...")

    # 清空现有数据
    Question.objects.all().delete()
    Option.objects.all().delete()

    # 问题数据
    questions_data = [
        {
            "question_text": "我们第一次约会，你会选择带我去哪里呢？",
            "scenario_image": "/static/images/scenarios/1_cafe.jpg",
            "order": 1,
            "options": [
                {
                    "option_text": "安静的美术馆看画展",
                    "preference_vector": [0.9, 0.2, 0.3, 0.1, 0.4, 0.8, 0.5],
                    "order": 1
                },
                {
                    "option_text": "热闹的游乐园玩过山车",
                    "preference_vector": [0.2, 0.9, 0.8, 0.7, 0.7, 0.3, 0.6],
                    "order": 2
                },
                {
                    "option_text": "神秘的密室逃脱",
                    "preference_vector": [0.5, 0.7, 0.6, 0.4, 0.9, 0.6, 0.8],
                    "order": 3
                },
                {
                    "option_text": "温馨的咖啡馆聊天",
                    "preference_vector": [0.1, 0.3, 0.2, 0.2, 0.2, 0.4, 0.3],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "今天的约会你想怎么安排呢？",
            "scenario_image": "/static/images/scenarios/2_schedule.jpg",
            "order": 2,
            "options": [
                {
                    "option_text": "慢节奏，一个地方待一整天",
                    "preference_vector": [0.8, 0.1, 0.4, 0.2, 0.3, 0.7, 0.6],
                    "order": 1
                },
                {
                    "option_text": "紧凑一点，多去几个地方",
                    "preference_vector": [0.3, 0.9, 0.7, 0.6, 0.6, 0.4, 0.5],
                    "order": 2
                },
                {
                    "option_text": "随性一点，走到哪算哪",
                    "preference_vector": [0.6, 0.5, 0.5, 0.3, 0.4, 0.5, 0.7],
                    "order": 3
                },
                {
                    "option_text": "提前做好详细的行程表",
                    "preference_vector": [0.4, 0.6, 0.3, 0.5, 0.8, 0.6, 0.4],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "到餐厅了，你会点什么口味的菜呢？",
            "scenario_image": "/static/images/scenarios/3_restaurant.jpg",
            "order": 3,
            "options": [
                {
                    "option_text": "酸甜口味的家常菜",
                    "preference_vector": [0.2, 0.4, 0.2, 0.3, 0.3, 0.5, 0.4],
                    "order": 1
                },
                {
                    "option_text": "麻辣刺激的川菜",
                    "preference_vector": [0.5, 0.8, 0.9, 0.6, 0.8, 0.4, 0.7],
                    "order": 2
                },
                {
                    "option_text": "清淡养生的粤菜",
                    "preference_vector": [0.7, 0.3, 0.1, 0.2, 0.2, 0.6, 0.3],
                    "order": 3
                },
                {
                    "option_text": "精致的西餐",
                    "preference_vector": [0.4, 0.5, 0.4, 0.8, 0.5, 0.7, 0.6],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "我们去看电影吧，你会选哪一种？",
            "scenario_image": "/static/images/scenarios/4_cinema.jpg",
            "order": 4,
            "options": [
                {
                    "option_text": "大制作商业大片",
                    "preference_vector": [0.3, 0.8, 0.7, 0.9, 0.7, 0.5, 0.6],
                    "order": 1
                },
                {
                    "option_text": "小众独立电影",
                    "preference_vector": [0.9, 0.3, 0.4, 0.1, 0.5, 0.8, 0.7],
                    "order": 2
                },
                {
                    "option_text": "经典老片重映",
                    "preference_vector": [0.7, 0.5, 0.5, 0.4, 0.6, 0.7, 0.5],
                    "order": 3
                },
                {
                    "option_text": "最新上映的动画片",
                    "preference_vector": [0.4, 0.6, 0.3, 0.5, 0.4, 0.3, 0.4],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "如果我们在约会中意见不一致，你会怎么做？",
            "scenario_image": "/static/images/scenarios/5_conflict.jpg",
            "order": 5,
            "options": [
                {
                    "option_text": "直接说出自己的想法，坦诚沟通",
                    "preference_vector": [0.5, 0.6, 0.6, 0.5, 0.9, 0.6, 0.5],
                    "order": 1
                },
                {
                    "option_text": "先妥协迁就对方，以后再说",
                    "preference_vector": [0.6, 0.4, 0.5, 0.3, 0.2, 0.7, 0.8],
                    "order": 2
                },
                {
                    "option_text": "用幽默的方式化解矛盾",
                    "preference_vector": [0.2, 0.7, 0.4, 0.4, 0.5, 0.4, 0.4],
                    "order": 3
                },
                {
                    "option_text": "冷静下来，理性分析问题",
                    "preference_vector": [0.4, 0.5, 0.3, 0.6, 0.8, 0.8, 0.6],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "如果我送你礼物，你更喜欢哪一种？",
            "scenario_image": "/static/images/scenarios/6_gift.jpg",
            "order": 6,
            "options": [
                {
                    "option_text": "实用的日常用品",
                    "preference_vector": [0.3, 0.5, 0.4, 0.4, 0.6, 0.2, 0.4],
                    "order": 1
                },
                {
                    "option_text": "有纪念意义的手工制品",
                    "preference_vector": [0.8, 0.3, 0.3, 0.2, 0.4, 0.9, 0.7],
                    "order": 2
                },
                {
                    "option_text": "酷炫的科技产品",
                    "preference_vector": [0.4, 0.8, 0.6, 0.8, 0.7, 0.7, 0.5],
                    "order": 3
                },
                {
                    "option_text": "精美的艺术品",
                    "preference_vector": [0.9, 0.2, 0.2, 0.3, 0.3, 0.8, 0.6],
                    "order": 4
                }
            ]
        },
        {
            "question_text": "约会结束了，你希望怎么告别？",
            "scenario_image": "/static/images/scenarios/7_goodbye.jpg",
            "order": 7,
            "options": [
                {
                    "option_text": "依依不舍，聊到很晚",
                    "preference_vector": [0.6, 0.4, 0.5, 0.3, 0.5, 0.7, 0.9],
                    "order": 1
                },
                {
                    "option_text": "约定下次见面的时间",
                    "preference_vector": [0.4, 0.6, 0.6, 0.5, 0.6, 0.5, 0.2],
                    "order": 2
                },
                {
                    "option_text": "给一个拥抱，然后转身离开",
                    "preference_vector": [0.7, 0.3, 0.4, 0.2, 0.4, 0.8, 0.8],
                    "order": 3
                },
                {
                    "option_text": "送我到家楼下，看着我上楼",
                    "preference_vector": [0.2, 0.5, 0.2, 0.4, 0.3, 0.6, 0.1],
                    "order": 4
                }
            ]
        }
    ]

    # 插入数据
    for q_data in questions_data:
        options_data = q_data.pop('options')
        question = Question.objects.create(**q_data)

        for o_data in options_data:
            Option.objects.create(question=question, **o_data)

    print("问题和选项数据填充完成！")


def populate_personalities():
    """填充人格画像数据"""
    print("正在填充人格画像数据...")

    # 清空现有数据
    Personality.objects.all().delete()

    # 人格数据
    personalities_data = [
        {
            "name": "钢铁侠型",
            "character_name": "托尼·斯塔克",
            "movie_name": "钢铁侠",
            "character_image": "/static/images/characters/ironman.jpg",
            "core_traits": "自信张扬、聪明绝顶、责任感强、外冷内热",
            "interpretation": "你就像钢铁侠托尼·斯塔克一样，表面玩世不恭，内心却有着强烈的责任感。你聪明机智，总能在关键时刻想出解决问题的办法，虽然有时会显得有些自负，但你的才华和勇气让人无法忽视。",
            "suitable_genres": "科幻片、超级英雄电影、高智商犯罪片",
            "match_threshold": [0.4, 0.8, 0.7, 0.8, 0.7, 0.7, 0.5]
        },
        {
            "name": "千寻型",
            "character_name": "荻野千寻",
            "movie_name": "千与千寻",
            "character_image": "/static/images/characters/chihiro.jpg",
            "core_traits": "善良勇敢、坚韧不拔、纯真善良、懂得感恩",
            "interpretation": "你拥有像千寻一样纯净的心灵，即使在陌生的环境中也能保持善良和勇敢。你看似柔弱，实则内心无比坚强，总能用自己的真诚和努力打动身边的人。",
            "suitable_genres": "治愈系动画、奇幻冒险片、成长励志片",
            "match_threshold": [0.5, 0.4, 0.3, 0.3, 0.4, 0.5, 0.4]
        },
        {
            "name": "教父型",
            "character_name": "维托·柯里昂",
            "movie_name": "教父",
            "character_image": "/static/images/characters/godfather.jpg",
            "core_traits": "沉稳内敛、深谋远虑、重情重义、有领导力",
            "interpretation": "你就像教父维托·柯里昂一样，沉稳冷静，不轻易表露情绪，但内心有着清晰的原则和底线。你重情重义，对家人和朋友无比忠诚，有着天生的领导气质。",
            "suitable_genres": "黑帮片、史诗片、权谋片",
            "match_threshold": [0.6, 0.5, 0.5, 0.5, 0.8, 0.7, 0.6]
        },
        {
            "name": "阿甘型",
            "character_name": "福雷斯·甘",
            "movie_name": "阿甘正传",
            "character_image": "/static/images/characters/forrest.jpg",
            "core_traits": "单纯执着、坚持不懈、真诚善良、运气极佳",
            "interpretation": "你拥有阿甘一样简单而纯粹的内心，认定一件事就会坚持不懈地去做。你真诚善良，从不计较得失，这种简单的力量往往能创造出意想不到的奇迹。",
            "suitable_genres": "励志片、温情片、传记片",
            "match_threshold": [0.3, 0.5, 0.4, 0.4, 0.5, 0.2, 0.3]
        },
        {
            "name": "赫敏型",
            "character_name": "赫敏·格兰杰",
            "movie_name": "哈利·波特",
            "character_image": "/static/images/characters/hermione.jpg",
            "core_traits": "聪明好学、理性冷静、勇敢正直、有正义感",
            "interpretation": "你就像赫敏一样，聪明好学，知识渊博，总是能在关键时刻提供帮助。你理性冷静，做事有条理，有着强烈的正义感，愿意为了正确的事情挺身而出。",
            "suitable_genres": "奇幻片、推理片、校园青春片",
            "match_threshold": [0.5, 0.6, 0.4, 0.5, 0.8, 0.8, 0.5]
        },
        {
            "name": "杰克型",
            "character_name": "杰克·道森",
            "movie_name": "泰坦尼克号",
            "character_image": "/static/images/characters/jack.jpg",
            "core_traits": "自由奔放、浪漫多情、热爱生活、敢于牺牲",
            "interpretation": "你拥有杰克一样自由不羁的灵魂，热爱生活，享受当下。你浪漫多情，愿意为了爱情付出一切，你的热情和活力总能感染身边的每一个人。",
            "suitable_genres": "爱情片、灾难片、冒险片",
            "match_threshold": [0.6, 0.5, 0.5, 0.4, 0.5, 0.8, 0.8]
        }
    ]

    # 插入数据
    for p_data in personalities_data:
        Personality.objects.create(**p_data)

    print("人格画像数据填充完成！")


def populate_movies_from_json():
    """从JSON文件填充电影数据"""
    print("正在填充电影数据...")

    # 清空现有数据
    Movie.objects.all().delete()

    # 读取JSON文件
    json_path = os.path.join(os.path.dirname(__file__), 'movies.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        movies_data = json.load(f)

    # 插入数据
    for m_data in movies_data:
        Movie.objects.create(**m_data)

    print(f"电影数据填充完成！共导入{len(movies_data)}部电影")


if __name__ == '__main__':
    populate_questions_and_options()
    populate_personalities()
    populate_movies_from_json()