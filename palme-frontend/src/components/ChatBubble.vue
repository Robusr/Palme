<template>
  <div class="chat-bubble">
    <div class="avatar">
      <img
        src="https://api.dicebear.com/7.x/avataaars/svg?seed=Palme"
        alt="头像"
        @error="handleImageError"
      >
    </div>
    <div class="bubble-content">
      <p>{{ displayedText }}</p>
      <span v-if="isTyping" class="typing-indicator">...</span>
    </div>
  </div>
</template>

<script setup>
import { toRef } from 'vue'
import { useTypewriter } from '../composables/useTypewriter'

const props = defineProps({
  text: {
    type: String,
    required: true
  }
})

// 使用toRef创建响应式引用，确保watch能正确触发
const textRef = toRef(props, 'text')
const { displayedText, isTyping } = useTypewriter(textRef, 40)

const handleImageError = (e) => {
  e.target.src = 'https://api.dicebear.com/7.x/avataaars/svg?seed=default'
}
</script>

<style scoped>
.chat-bubble {
  display: flex;
  align-items: flex-start;
  margin-bottom: 20px;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  overflow: hidden;
  margin-right: 12px;
  flex-shrink: 0;
  background: #667eea;
}

.avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.bubble-content {
  max-width: 70%;
  background: white;
  padding: 12px 16px;
  border-radius: 18px;
  border-top-left-radius: 4px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  position: relative;
}

.bubble-content p {
  font-size: 16px;
  line-height: 1.5;
  color: #333;
  margin: 0;
}

.typing-indicator {
  position: absolute;
  right: -20px;
  bottom: 8px;
  color: #999;
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 50% { opacity: 1; }
  51%, 100% { opacity: 0; }
}
</style>