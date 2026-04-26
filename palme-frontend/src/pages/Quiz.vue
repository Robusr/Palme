<template>
  <div class="quiz-container">
    <!-- 情景图片 -->
    <div class="scenario-image">
      <img :src="currentQuestion.scenario_image" alt="情景图" v-if="currentQuestion">
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
      <ChatBubble :text="currentQuestion.question_text" v-if="currentQuestion" />
    </div>

    <!-- 选项区域 -->
    <div class="options-area">
      <van-button
        v-for="option in currentQuestion?.options"
        :key="option.id"
        type="default"
        size="large"
        class="option-btn"
        @click="selectOption(option.id)"
        :loading="loading && quizStore.answers.length === 7"
      >
        {{ option.option_text }}
      </van-button>
    </div>
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

// 组件挂载时检查数据
onMounted(() => {
  if (questions.value.length === 0) {
    router.push('/')
  }
})

const selectOption = async (optionId) => {
  // 先添加当前题的答案
  quizStore.submitAnswer(optionId)

  // 检查是否已经答完了所有7道题
  if (quizStore.answers.length === 7) {
    await quizStore.submitAllAnswers()
    router.push('/result')
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