<script setup>
import { computed } from 'vue'
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

// 如果没有问题，跳回首页
if (questions.value.length === 0) {
  router.push('/')
}

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