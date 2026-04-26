# Palme 电影人格测试
> 华中科技大学科创实验班《数据科学与机器学习（一）》课程设计，
> 一款**浪漫约会交互风格**的沉浸式电影人格测评 Web 应用，
> 通过情景化答题，测算你的专属电影人格，搭配个性化电影推荐 & 一键分享海报，

<div align="center">
<img src="https://img.shields.io/badge/Vue-3.4-42b883" />
<img src="https://img.shields.io/badge/Vite-6.x-646cff" />
<img src="https://img.shields.io/badge/Django-5.x-092E20" />
<img src="https://img.shields.io/badge/Pinia-状态管理-yellow" />
<img src="https://img.shields.io/badge/Vant4-移动端组件-blue" />
<img src="https://img.shields.io/badge/MIT-License-red" />
</div>

## 📖 项目介绍
**Palme** 以「浪漫约会」为叙事载体，打造轻量治愈的心理测评体验：
- 7 道沉浸式情景选择题
- 6 种经典电影人格定位（千寻 / 教父 / 钢铁侠 / 阿甘 / 赫敏 / 杰克）
- 精准人格解读 + 标签化特质分析
- 智能匹配高分电影库，一键生成精美分享海报
- 全移动端适配、流畅动画交互、完善异常处理

整体采用 **紫渐变治愈系设计**，结合 Galgame 对话交互，告别传统枯燥测评。

## 🛠️ 技术栈
### 前端
- 核心框架：**Vue 3 + Vite**（组合式 API）
- 状态管理：**Pinia**
- UI 组件库：**Vant 4**
- 网络请求：Axios
- 海报生成：html2canvas
- 动画方案：原生 CSS3 / 自定义 Composables
- 样式：原生 CSS、弹性布局、响应式适配

### 后端
- 服务框架：**Django 5.x**
- 接口服务：Django REST Framework
- 数据库：MySQL
- 跨域处理：CORS
- 数据结构：标准化问卷 / 人格 / 电影结构化存储

## ✨ 核心功能
### 🔹 交互体验
- ✅ 对话气泡**打字机逐字效果**，模拟真实聊天
- ✅ 全局页面过渡动画（淡入/滑动切换）
- ✅ 选项渐入弹出动画 + 按钮点击缩放反馈
- ✅ 骨架屏占位加载、全局 Loading 指示器
- ✅ 移动端触摸优化、刘海屏/小黑条安全区域适配

### 🔹 业务核心
- ✅ 完整答题流程：会话创建 → 答题 → 答案提交 → 人格计算
- ✅ 多维度向量算法匹配电影人格
- ✅ 详细人格解析、核心特质标签、适配电影风格
- ✅ 海量电影库推荐，含评分/类型/简介弹窗
- ✅ 图片加载失败兜底占位图，杜绝破碎图标

### 🔹 拓展能力
- ✅ 网络请求自动重试（3 次重试机制）
- ✅ 一键生成高清分享海报，支持本地下载
- ✅ 独立人格专属渐变背景海报样式
- ✅ 结果重置、重新测试、社交分享能力

## 📁 项目结构
```
Palme/
├── palme-frontend/        # 前端 Vue 项目
│   ├── public/            # 静态资源（本地图片、静态文件）
│   ├── src/
│   │   ├── assets/        # 静态资源
│   │   ├── components/    # 公共组件
│   │   │   ├── ChatBubble.vue    # 对话气泡
│   │   │   ├── MovieCard.vue     # 电影卡片
│   │   │   ├── SkeletonLoader.vue # 骨架屏
│   │   │   └── SharePoster.vue   # 分享海报
│   │   ├── composables/   # 组合式工具
│   │   │   └── useTypewriter.js  # 打字机逻辑
│   │   ├── pages/         # 页面
│   │   │   ├── Home.vue   # 首页/开始页
│   │   │   ├── Quiz.vue   # 答题页
│   │   │   └── Result.vue # 结果页
│   │   ├── router/        # 路由配置
│   │   ├── stores/        # Pinia 状态管理
│   │   ├── utils/         # 工具函数 & 接口封装
│   │   └── App.vue / main.js # 入口文件
│   └── vite.config.js     # Vite 配置
│
├── Palme-backend/         # 后端 Django 项目
│   ├── palme_api/         # 业务应用
│   ├── data/              # 初始化数据脚本
│   ├── Palme/             # 项目配置
│   └── manage.py          # Django 入口
└── README.md              # 项目文档
```

## 🚀 快速启动
### 环境依赖
- Node.js >= 18.x
- Python >= 3.10
- MySQL 8.0+

### 1. 后端启动
```bash
# 进入后端目录
cd Palme-backend

# 安装依赖
pip install -r requirements.txt

# 初始化数据库数据
python data/initial_data.py

# 启动后端服务 (默认 8000 端口)
python manage.py runserver
```

### 2. 前端启动
```bash
# 进入前端目录
cd palme-frontend

# 安装依赖
npm install

# 启动开发环境 (默认 5173 端口)
npm run dev
```

访问：`http://localhost:5173` 即可进入项目

## 🎨 项目优化亮点
本项目经过多轮深度体验优化，解决生产级常见问题：
1. **性能优化**：定时器销毁、防止无限监听、DOM 强制刷新防重叠
2. **容错处理**：接口重试、图片降级、网络异常提示、路由守卫
3. **视觉优化**：全局统一动效、渐变主题、毛玻璃设计、层级阴影
4. **兼容性**：移动端全尺寸适配、iOS/Android 安全区域兼容
5. **工程规范**：模块化拆分、组合式逻辑复用、状态统一管理

## 📸 页面预览
| 首页 | 答题页 | 结果页 | 分享海报 |
|------|--------|--------|----------|
| 浪漫渐变首页 | 情景对话答题 | 人格分析报告 | 定制高清海报 |

> 可自行替换本地图片资源，无缝切换离线静态资源部署

## 📌 二次开发拓展方向
- 增加用户登录、历史记录本地缓存
- 扩充题库 & 新增更多电影人格
- 完善电影详情页、预告片跳转
- 增加背景音乐、答题音效
- 部署轻量化后端，打包静态页面上线
- 增加人格匹配、好友对比社交功能

## 📄 开源协议
本项目基于 **MIT 开源协议** 开源，仅供学习与个人非商业使用。
二次开发请保留项目原开源声明，禁止商用售卖。

## 🤝 致谢
感谢7-11便利店2.8CNY购买的COSTA阿萨姆红茶包，陪我整晚Coding