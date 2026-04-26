<template>
  <div class="home-container">
    <div class="home-content">
      <h1 class="title">Palme</h1>
      <p class="subtitle">通过一场浪漫的约会，发现你的电影人格</p>
      <van-button
        type="primary"
        size="large"
        class="start-btn"
        @click="startQuiz"
        :loading="loading"
      >
        开始约会
      </van-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue' // 添加这行！
import { useQuizStore } from '../stores/quizStore'
import { useRouter } from 'vue-router'

const quizStore = useQuizStore()
const router = useRouter()

const loading = ref(false)

const startQuiz = async () => {
  loading.value = true
  await quizStore.initQuiz()
  loading.value = false
  router.push('/quiz')
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
  margin-bottom: 60px;
  opacity: 0.9;
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