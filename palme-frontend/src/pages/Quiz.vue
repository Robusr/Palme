<template>
  <div class="quiz-container">
    <!-- 加载状态 -->
    <div v-if="!currentQuestion" class="loading-container">
      <van-loading size="large">加载中...</van-loading>
    </div>

    <!-- 正常内容 -->
    <template v-else>
      <!-- 情景图片 -->
      <div class="scenario-image">
        <img :src="getScenarioImage(currentQuestionIndex)" alt="情景图">
      </div>

      <!-- 进度条 -->
      <van-progress
        :percentage="(currentQuestionIndex + 1) * 100 / questions.length"
        class="progress-bar"
        color="#667eea"
        stroke-width="4"
      />

      <!-- 进度文字 -->
      <div class="progress-text">
        第 {{ currentQuestionIndex + 1 }} / {{ questions.length }} 题
      </div>

      <!-- 对话区域 -->
      <div class="chat-area">
        <ChatBubble :text="currentQuestion.question_text" />
      </div>

      <!-- 选项区域 -->
      <div class="options-area">
        <van-button
          v-for="option in currentQuestion.options"
          :key="option.id"
          type="default"
          size="large"
          class="option-btn"
          @click="selectOption(option.id)"
          :loading="loading && currentQuestionIndex === questions.length - 1"
        >
          {{ option.option_text }}
        </van-button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted } from 'vue'
import { useQuizStore } from '../stores/quizStore'
import { useRouter } from 'vue-router'
import ChatBubble from '../components/ChatBubble.vue'

const quizStore = useQuizStore()
const router = useRouter()

const questions = computed(() => quizStore.questions)
const currentQuestionIndex = computed(() => quizStore.currentQuestionIndex)
const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const loading = computed(() => quizStore.loading)

// 使用在线占位图
const getScenarioImage = (index) => {
  const images = [
    'https://picsum.photos/seed/cafe/800/600',
    'https://picsum.photos/seed/schedule/800/600',
    'https://picsum.photos/seed/restaurant/800/600',
    'https://picsum.photos/seed/cinema/800/600',
    'https://picsum.photos/seed/conflict/800/600',
    'https://picsum.photos/seed/gift/800/600',
    'https://picsum.photos/seed/goodbye/800/600'
  ]
  return images[index] || images[0]
}

// 组件挂载时检查数据
onMounted(() => {
  console.log('Quiz组件挂载')
  console.log('questions:', questions.value)
  console.log('currentQuestionIndex:', currentQuestionIndex.value)

  if (questions.value.length === 0) {
    console.log('没有问题数据，跳回首页')
    router.push('/')
  }
})

const selectOption = async (optionId) => {
  console.log('选择选项:', optionId)
  console.log('当前答案数量:', quizStore.answers.length)

  // 先添加当前题的答案
  quizStore.submitAnswer(optionId)

  console.log('添加后答案数量:', quizStore.answers.length)

  // 检查是否已经答完了所有7道题
  if (quizStore.answers.length === 7) {
    console.log('答完7题，提交答案...')
    try {
      await quizStore.submitAllAnswers()
      console.log('提交成功，跳转到结果页')
      router.push('/result')
    } catch (error) {
      console.error('提交失败:', error)
      alert('提交失败，请重试')
    }
  }
}
</script>

<style scoped>
.quiz-container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  background: #f5f5f5;
}

.loading-container {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

.scenario-image {
  width: 100%;
  height: 35%;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.scenario-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.progress-bar {
  margin: 10px 20px 5px;
}

.progress-text {
  text-align: center;
  font-size: 14px;
  color: #666;
  margin-bottom: 10px;
}

.chat-area {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}

.options-area {
  padding: 20px;
  background: white;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
}

.option-btn {
  width: 100%;
  margin-bottom: 12px;
  text-align: left;
  padding: 15px 20px;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  background: white;
  color: #333;
}

.option-btn:last-child {
  margin-bottom: 0;
}

.option-btn:active {
  background: #f0f0f0;
}
</style>