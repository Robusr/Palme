<template>
  <div class="quiz-container">
    <!-- 只在数据未加载时显示骨架屏 -->
    <SkeletonLoader v-if="!currentQuestion" type="quiz" />

    <template v-else>
      <!-- 情景图片：添加key强制重新渲染 -->
      <div class="scenario-image" :key="currentQuestionIndex">
        <img
          :src="currentQuestion.scenario_image"
          alt="情景图"
          @error="handleImageError"
        >
      </div>

      <!-- 进度条 -->
      <van-progress
        :percentage="Math.round((currentQuestionIndex + 1) * 100 / questions.length)"
        class="progress-bar"
        color="#667eea"
        stroke-width="4"
      />

      <!-- 进度文字 -->
      <div class="progress-text">
        第 {{ currentQuestionIndex + 1 }} / {{ questions.length }} 题
      </div>

      <!-- 对话区域：添加key强制重新渲染 -->
      <div class="chat-area" :key="`chat-${currentQuestionIndex}`">
        <ChatBubble :text="currentQuestion.question_text" />
      </div>

      <!-- 选项区域：移除transition-group，改用简单v-for -->
      <div class="options-area">
        <van-button
          v-for="option in currentQuestion.options"
          :key="`${currentQuestionIndex}-${option.id}`"
          type="default"
          size="large"
          class="option-btn"
          @click="selectOption(option.id)"
          :loading="submitting"
          :disabled="submitting"
        >
          {{ option.option_text }}
        </van-button>
      </div>
    </template>
  </div>
</template>

<script setup>
import { computed, onMounted, ref, nextTick } from 'vue'
import { useQuizStore } from '../stores/quizStore'
import { useRouter } from 'vue-router'
import ChatBubble from '../components/ChatBubble.vue'
import SkeletonLoader from '../components/SkeletonLoader.vue'
import { useLoadingStore } from '../stores/loadingStore'

const quizStore = useQuizStore()
const router = useRouter()
const loadingStore = useLoadingStore()

const questions = computed(() => quizStore.questions)
const currentQuestionIndex = computed(() => quizStore.currentQuestionIndex)
const currentQuestion = computed(() => questions.value[currentQuestionIndex.value])
const submitting = ref(false)

// 图片加载失败处理
const handleImageError = (e) => {
  e.target.src = 'https://picsum.photos/seed/default/800/600'
}

// 组件挂载时检查数据
onMounted(() => {
  if (questions.value.length === 0) {
    router.push('/')
  }
})

const selectOption = async (optionId) => {
  if (submitting.value) return

  // 添加点击反馈
  const btn = event.target.closest('.option-btn')
  btn.style.transform = 'scale(0.95)'
  setTimeout(() => {
    btn.style.transform = 'scale(1)'
  }, 100)

  // 先添加当前题的答案
  quizStore.submitAnswer(optionId)

  // 检查是否已经答完了所有7道题
  if (quizStore.answers.length === 7) {
    submitting.value = true
    loadingStore.showLoading('正在分析你的人格...')

    try {
      await quizStore.submitAllAnswers()
      router.push('/result')
    } catch (error) {
      console.error('提交失败:', error)
    } finally {
      submitting.value = false
      loadingStore.hideLoading()
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
  /* 防止页面滚动 */
  overflow: hidden;
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
  transition: opacity 0.3s ease;
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
  /* 触摸优化：增大点击区域 */
  min-height: 48px;
  transition: all 0.2s ease;
}

.option-btn:last-child {
  margin-bottom: 0;
}

.option-btn:hover {
  background: #f8f8f8;
  border-color: #667eea;
}

.option-btn:active {
  background: #f0f0f0;
  transform: scale(0.98);
}
</style>