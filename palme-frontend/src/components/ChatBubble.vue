<template>
  <div class="chat-bubble">
    <div class="avatar">
      <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Palme" alt="头像">
    </div>
    <div class="bubble-content">
      <p>{{ text }}</p>
    </div>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    required: true
  }
})
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
}

.bubble-content p {
  font-size: 16px;
  line-height: 1.5;
  color: #333;
}
</style>