<template>
  <div class="skeleton-loader">
    <!-- 答题页骨架屏 -->
    <template v-if="type === 'quiz'">
      <div class="skeleton-scenario"></div>
      <div class="skeleton-progress"></div>
      <div class="skeleton-chat">
        <div class="skeleton-avatar"></div>
        <div class="skeleton-bubble"></div>
      </div>
      <div class="skeleton-options">
        <div class="skeleton-option" v-for="i in 4" :key="i"></div>
      </div>
    </template>

    <!-- 结果页骨架屏 -->
    <template v-if="type === 'result'">
      <div class="skeleton-result-header">
        <div class="skeleton-avatar-large"></div>
        <div class="skeleton-title"></div>
        <div class="skeleton-subtitle"></div>
        <div class="skeleton-text"></div>
        <div class="skeleton-text"></div>
      </div>
      <div class="skeleton-movies">
        <div class="skeleton-movie-card" v-for="i in 4" :key="i">
          <div class="skeleton-movie-poster"></div>
          <div class="skeleton-movie-title"></div>
          <div class="skeleton-movie-meta"></div>
        </div>
      </div>
    </template>
  </div>
</template>

<script setup>
defineProps({
  type: {
    type: String,
    default: 'quiz'
  }
})
</script>

<style scoped>
.skeleton-loader {
  width: 100%;
  height: 100%;
  background: #f5f5f5;
}

.skeleton-scenario {
  width: 100%;
  height: 35%;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

.skeleton-progress {
  height: 4px;
  margin: 10px 20px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  border-radius: 2px;
}

.skeleton-chat {
  display: flex;
  padding: 20px;
  align-items: flex-start;
}

.skeleton-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
  margin-right: 12px;
}

.skeleton-bubble {
  width: 70%;
  height: 60px;
  border-radius: 18px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

.skeleton-options {
  padding: 20px;
}

.skeleton-option {
  width: 100%;
  height: 50px;
  margin-bottom: 12px;
  border-radius: 12px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

.skeleton-result-header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 30px 20px;
  text-align: center;
}

.skeleton-avatar-large {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  background: rgba(255,255,255,0.2);
  margin: 0 auto 20px;
  animation: shimmer 1.5s infinite;
}

.skeleton-title {
  width: 120px;
  height: 32px;
  margin: 0 auto 8px;
  background: rgba(255,255,255,0.2);
  border-radius: 4px;
  animation: shimmer 1.5s infinite;
}

.skeleton-subtitle {
  width: 180px;
  height: 18px;
  margin: 0 auto 16px;
  background: rgba(255,255,255,0.2);
  border-radius: 4px;
  animation: shimmer 1.5s infinite;
}

.skeleton-text {
  width: 80%;
  height: 16px;
  margin: 0 auto 8px;
  background: rgba(255,255,255,0.2);
  border-radius: 4px;
  animation: shimmer 1.5s infinite;
}

.skeleton-movies {
  padding: 20px;
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.skeleton-movie-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
}

.skeleton-movie-poster {
  width: 100%;
  height: 180px;
  background: linear-gradient(90deg, #f0f0f0 25%, #e0e0e0 50%, #f0f0f0 75%);
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

.skeleton-movie-title {
  width: 80%;
  height: 14px;
  margin: 12px 12px 4px;
  background: #f0f0f0;
  border-radius: 2px;
  animation: shimmer 1.5s infinite;
}

.skeleton-movie-meta {
  width: 60%;
  height: 12px;
  margin: 0 12px 12px;
  background: #f0f0f0;
  border-radius: 2px;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% {
    background-position: 200% 0;
  }
  100% {
    background-position: -200% 0;
  }
}
</style>