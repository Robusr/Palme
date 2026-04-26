<template>
  <div class="result-container" v-if="result">
    <!-- 人格画像部分 -->
    <div class="personality-section">
      <div class="character-image">
        <img :src="getCharacterImage(result.personality.name)" alt="角色图">
      </div>
      <h2 class="personality-name">{{ result.personality.name }}</h2>
      <h3 class="character-name">{{ result.personality.character_name }} · {{ result.personality.movie_name }}</h3>
      <p class="core-traits">{{ result.personality.core_traits }}</p>
      <div class="interpretation">
        <p>{{ result.personality.interpretation }}</p>
      </div>
      <p class="suitable-genres">最适配电影风格：{{ result.personality.suitable_genres }}</p>
    </div>

    <!-- 推荐电影部分 -->
    <div class="movies-section">
      <h3 class="section-title">为你推荐的电影</h3>
      <div class="movies-list">
        <MovieCard v-for="movie in result.movies" :key="movie.id" :movie="movie" />
      </div>
    </div>

    <!-- 操作按钮 -->
    <div class="action-buttons">
      <van-button type="default" size="large" @click="resetQuiz">重新测试</van-button>
      <van-button type="primary" size="large" @click="shareResult">分享结果</van-button>
    </div>
  </div>

  <van-loading v-else size="large" class="loading" />
</template>

<script setup>
import { computed } from 'vue' // 添加这行！
import { useQuizStore } from '../stores/quizStore'
import { useRouter } from 'vue-router'
import MovieCard from '../components/MovieCard.vue'
import { showToast } from 'vant'

const quizStore = useQuizStore()
const router = useRouter()

const result = computed(() => quizStore.result)

// 使用在线占位图
const getCharacterImage = (name) => {
  const seed = name.replace(/\s/g, '')
  return `https://api.dicebear.com/7.x/avataaars/svg?seed=${seed}`
}

// 如果没有结果，跳回首页
if (!result.value) {
  router.push('/')
}

const resetQuiz = () => {
  quizStore.resetQuiz()
  router.push('/')
}

const shareResult = () => {
  showToast('分享功能开发中...')
}
</script>

<style scoped>
.result-container {
  width: 100%;
  height: 100%;
  overflow-y: auto;
  background: #f5f5f5;
  padding-bottom: 100px;
}

.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.personality-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 30px 20px;
  text-align: center;
}

.character-image {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  overflow: hidden;
  margin: 0 auto 20px;
  border: 4px solid white;
  box-shadow: 0 4px 15px rgba(0,0,0,0.2);
  background: white;
}

.character-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.personality-name {
  font-size: 28px;
  font-weight: bold;
  margin-bottom: 8px;
}

.character-name {
  font-size: 18px;
  opacity: 0.9;
  margin-bottom: 16px;
}

.core-traits {
  font-size: 16px;
  margin-bottom: 20px;
  font-style: italic;
}

.interpretation {
  background: rgba(255,255,255,0.1);
  padding: 16px;
  border-radius: 12px;
  margin-bottom: 16px;
  text-align: left;
  line-height: 1.6;
}

.suitable-genres {
  font-size: 14px;
  opacity: 0.9;
}

.movies-section {
  padding: 20px;
}

.section-title {
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #333;
}

.movies-list {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.action-buttons {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  padding: 16px;
  background: white;
  box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
  gap: 12px;
}

.action-buttons .van-button {
  flex: 1;
}
</style>