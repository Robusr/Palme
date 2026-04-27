<template>
  <div class="home-container">
    <!-- 背景装饰 -->
    <div class="background-decoration">
      <div class="decoration-circle circle-1"></div>
      <div class="decoration-circle circle-2"></div>
      <div class="decoration-circle circle-3"></div>
      <div class="decoration-circle circle-4"></div>
    </div>

    <div class="home-content">
      <div class="logo-container">
        <div class="logo-icon">🎬</div>
        <h1 class="title">Palme</h1>
      </div>

      <p class="subtitle">通过一场浪漫的约会</p>
      <p class="subtitle">发现你的专属电影人格</p>
      <p class="subtitle">Powered By Robusr</p>

      <div class="features">
        <div class="feature-item">
          <span class="feature-icon">✨</span>
          <span>7道精心设计的题目</span>
        </div>
        <div class="feature-item">
          <span class="feature-icon">🎭</span>
          <span>6种经典电影人格</span>
        </div>
        <div class="feature-item">
          <span class="feature-icon">🎥</span>
          <span>个性化电影推荐</span>
        </div>
      </div>

      <van-button
          type="primary"
          size="large"
          class="start-btn"
          @click="startQuiz"
          :loading="loading"
      >
        开始约会
      </van-button>

      <p class="hint">测试时长约2分钟</p>
    </div>
  </div>
</template>

<script setup>
import {ref} from 'vue'
import {useQuizStore} from '../stores/quizStore'
import {useRouter} from 'vue-router'
import {useLoadingStore} from '../stores/loadingStore'

const quizStore = useQuizStore()
const router = useRouter()
const loadingStore = useLoadingStore()

const loading = ref(false)

const startQuiz = async () => {
  loading.value = true
  loadingStore.showLoading('正在准备约会...')

  try {
    await quizStore.initQuiz()
    // 成功后隐藏全局加载，然后跳转
    loadingStore.hideLoading()
    router.push('/quiz')
  } catch (error) {
    console.error('初始化失败:', error)
    loadingStore.hideLoading()
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.home-container {
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
}

.background-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  animation: float 6s ease-in-out infinite;
}

.circle-1 {
  width: 200px;
  height: 200px;
  top: -50px;
  right: -50px;
  animation-delay: 0s;
}

.circle-2 {
  width: 150px;
  height: 150px;
  top: 30%;
  left: -30px;
  animation-delay: 1s;
}

.circle-3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  right: 20%;
  animation-delay: 2s;
}

.circle-4 {
  width: 80px;
  height: 80px;
  bottom: -20px;
  left: 30%;
  animation-delay: 3s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(5deg);
  }
}

.home-content {
  text-align: center;
  color: white;
  padding: 0 20px;
  position: relative;
  z-index: 1;
}

.logo-container {
  margin-bottom: 30px;
}

.logo-icon {
  font-size: 80px;
  margin-bottom: 10px;
  animation: bounce 2s ease-in-out infinite;
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

.title {
  font-size: 56px;
  font-weight: 900;
  margin-bottom: 10px;
  text-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
  letter-spacing: 8px;
}

.subtitle {
  font-size: 20px;
  margin-bottom: 8px;
  opacity: 0.95;
  font-weight: 300;
}

.features {
  margin: 40px 0;
  text-align: left;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  padding: 20px;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.feature-item {
  display: flex;
  align-items: center;
  margin-bottom: 12px;
  font-size: 16px;
}

.feature-item:last-child {
  margin-bottom: 0;
}

.feature-icon {
  margin-right: 12px;
  font-size: 20px;
}

.start-btn {
  width: 240px;
  height: 60px;
  border-radius: 30px;
  font-size: 20px;
  font-weight: 600;
  background: white;
  color: #667eea;
  border: none;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
}

.start-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.3);
}

.start-btn:active {
  transform: translateY(0);
}

.hint {
  margin-top: 20px;
  font-size: 14px;
  opacity: 0.7;
}
</style>