<template>
  <div class="home-container">
    <div class="home-content">
      <h1 class="title">Palme</h1>
      <p class="subtitle">通过一场浪漫的约会，发现你的电影人格</p>

      <div v-if="errorMessage" class="error-message">
        {{ errorMessage }}
      </div>

      <van-button
        type="primary"
        size="large"
        class="start-btn"
        @click="startQuiz"
        :loading="loading"
        :disabled="loading"
      >
        {{ loading ? '加载中...' : '开始约会' }}
      </van-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useQuizStore } from '../stores/quizStore'
import { useRouter } from 'vue-router'

const quizStore = useQuizStore()
const router = useRouter()

const loading = ref(false)
const errorMessage = ref('')

const startQuiz = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    console.log('开始初始化...')
    await quizStore.initQuiz()
    console.log('初始化完成，questions:', quizStore.questions)

    if (quizStore.questions.length === 0) {
      throw new Error('没有获取到问题数据')
    }

    router.push('/quiz')
  } catch (error) {
    console.error('初始化失败:', error)
    errorMessage.value = error.message || '初始化失败，请检查后端是否启动'
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
}

.home-content {
  text-align: center;
  color: white;
  padding: 0 20px;
}

.title {
  font-size: 48px;
  font-weight: bold;
  margin-bottom: 20px;
  text-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.subtitle {
  font-size: 18px;
  margin-bottom: 30px;
  opacity: 0.9;
}

.error-message {
  background: rgba(255,0,0,0.2);
  border: 1px solid rgba(255,255,255,0.3);
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 20px;
  font-size: 14px;
}

.start-btn {
  width: 200px;
  height: 50px;
  border-radius: 25px;
  font-size: 18px;
  background: white;
  color: #667eea;
  border: none;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
}
</style>