# -*- coding: utf-8 -*-
"""
@File    : initial_data.py
@Author  : Robusr
@Date    : 2026/4/27 02:48
@Description: 初始数据填充脚本
@Software: PyCharm
"""
import os
import sys
import django
import json

# 添加项目根目录到 Python 路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 设置 Django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Palme.settings')
django.setup()

from palme_api.models import Question, Option, Personality, Movie


def populate_questions_and_options():
    print("正在填充问题和选项数据...")

    # 清空现有数据
    Question.objects.all().delete()
    Option.objects.all().delete()

    # 完整的7道题数据
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
    print("正在填充电影数据...")

    # 清空现有数据
    Movie.objects.all().delete()

    # 读取JSON文件
    json_path = os.path.join(os.path.dirname(__file__), 'movies.json')

    # 检查文件是否存在
    if not os.path.exists(json_path):
        print(f"警告: {json_path} 文件不存在，将创建示例电影数据")
        # 创建示例电影数据
        movies_data = [
            {
                "title": "钢铁侠",
                "poster": "/static/images/posters/ironman.jpg",
                "genres": "科幻/动作/冒险",
                "douban_rating": 8.4,
                "release_year": 2008,
                "director": "乔恩·费儒",
                "summary": "托尼·斯塔克是一位天才发明家，也是一位亿万富翁。在一次被绑架的经历中，他制造了一套高科技盔甲，从此化身钢铁侠，开始了他的超级英雄生涯。",
                "feature_vector": [0.3, 0.9, 0.8, 0.9, 0.7, 0.7, 0.5]
            },
            {
                "title": "千与千寻",
                "poster": "/static/images/posters/spiritedaway.jpg",
                "genres": "动画/奇幻/冒险",
                "douban_rating": 9.4,
                "release_year": 2001,
                "director": "宫崎骏",
                "summary": "千寻和父母在搬家途中误入了一个神秘的世界。父母因为贪吃变成了猪，千寻为了救父母，在汤婆婆的澡堂里工作，经历了一系列奇妙的冒险。",
                "feature_vector": [0.5, 0.4, 0.3, 0.3, 0.4, 0.5, 0.4]
            },
            {
                "title": "教父",
                "poster": "/static/images/posters/godfather.jpg",
                "genres": "剧情/犯罪",
                "douban_rating": 9.3,
                "release_year": 1972,
                "director": "弗朗西斯·福特·科波拉",
                "summary": "柯里昂家族是美国最有权势的黑手党家族之一。教父维托·柯里昂深受人们的尊敬，但也树敌众多。当他遭遇暗杀后，他的小儿子迈克不得不接手家族事务。",
                "feature_vector": [0.6, 0.5, 0.5, 0.5, 0.8, 0.7, 0.6]
            },
            {
                "title": "阿甘正传",
                "poster": "/static/images/posters/forrestgump.jpg",
                "genres": "剧情/爱情",
                "douban_rating": 9.5,
                "release_year": 1994,
                "director": "罗伯特·泽米吉斯",
                "summary": "阿甘是一个智商只有75的低能儿，但他的一生却充满了传奇色彩。他参加了越战，成为了乒乓球明星，甚至成为了亿万富翁。",
                "feature_vector": [0.3, 0.5, 0.4, 0.4, 0.5, 0.2, 0.3]
            },
            {
                "title": "哈利·波特与魔法石",
                "poster": "/static/images/posters/harrypotter1.jpg",
                "genres": "奇幻/冒险",
                "douban_rating": 9.2,
                "release_year": 2001,
                "director": "克里斯·哥伦布",
                "summary": "哈利·波特是一个孤儿，从小被姨妈一家收养。在他11岁生日那天，他得知自己是一名巫师，并被邀请到霍格沃茨魔法学校学习。",
                "feature_vector": [0.5, 0.6, 0.4, 0.5, 0.8, 0.8, 0.5]
            },
            {
                "title": "泰坦尼克号",
                "poster": "/static/images/posters/titanic.jpg",
                "genres": "剧情/爱情/灾难",
                "douban_rating": 9.5,
                "release_year": 1997,
                "director": "詹姆斯·卡梅隆",
                "summary": "1912年，泰坦尼克号从英国南安普顿出发驶往美国纽约。在船上，穷画家杰克和贵族少女露丝相遇并相爱了。然而，这艘巨轮却在途中撞上了冰山。",
                "feature_vector": [0.6, 0.5, 0.5, 0.4, 0.5, 0.8, 0.8]
            },
            {
                "title": "肖申克的救赎",
                "poster": "/static/images/posters/shawshank.jpg",
                "genres": "剧情/犯罪",
                "douban_rating": 9.7,
                "release_year": 1994,
                "director": "弗兰克·德拉邦特",
                "summary": "银行家安迪被冤枉杀害了妻子和她的情人，被判处终身监禁。在肖申克监狱里，他结识了瑞德，并开始了长达19年的越狱计划。",
                "feature_vector": [0.7, 0.4, 0.6, 0.3, 0.7, 0.6, 0.7]
            },
            {
                "title": "盗梦空间",
                "poster": "/static/images/posters/inception.jpg",
                "genres": "科幻/悬疑/动作",
                "douban_rating": 9.4,
                "release_year": 2010,
                "director": "克里斯托弗·诺兰",
                "summary": "道姆·柯布是一位经验丰富的盗梦者，他能够潜入别人的梦境，窃取他们潜意识中的秘密。为了回到自己的孩子身边，他接受了一项几乎不可能完成的任务。",
                "feature_vector": [0.5, 0.8, 0.7, 0.8, 0.9, 0.8, 0.9]
            },
            {
                "title": "星际穿越",
                "poster": "/static/images/posters/interstellar.jpg",
                "genres": "科幻/剧情/冒险",
                "douban_rating": 9.4,
                "release_year": 2014,
                "director": "克里斯托弗·诺兰",
                "summary": "在不久的将来，地球面临着严重的环境危机。前NASA宇航员库珀接受了一项秘密任务，带领一支小队穿越虫洞，寻找适合人类居住的新星球。",
                "feature_vector": [0.4, 0.7, 0.6, 0.9, 0.6, 0.7, 0.8]
            },
            {
                "title": "楚门的世界",
                "poster": "/static/images/posters/trumanshow.jpg",
                "genres": "剧情/科幻",
                "douban_rating": 9.4,
                "release_year": 1998,
                "director": "彼得·威尔",
                "summary": "楚门从出生起就生活在一个巨大的摄影棚里，他的一举一动都被直播给全世界的观众。直到有一天，他发现了这个秘密，并决定逃离这个虚假的世界。",
                "feature_vector": [0.6, 0.6, 0.5, 0.4, 0.7, 0.5, 0.8]
            }
        ]
    else:
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