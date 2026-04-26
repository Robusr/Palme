<template>
  <div class="movie-card" @click="showDetail">
    <div class="poster">
      <img
        :src="movie.poster"
        alt="电影海报"
        @error="handleImageError"
      >
    </div>
    <div class="info">
      <h4 class="title">{{ movie.title }}</h4>
      <div class="meta">
        <span class="rating">★ {{ movie.douban_rating }}</span>
        <span class="year">{{ movie.release_year }}</span>
      </div>
      <p class="genres">{{ movie.genres }}</p>
    </div>
  </div>
</template>

<script setup>
import { showDialog } from 'vant'

const props = defineProps({
  movie: {
    type: Object,
    required: true
  }
})

const handleImageError = (e) => {
  e.target.src = 'https://picsum.photos/seed/movie/300/450'
}

const showDetail = () => {
  showDialog({
    title: props.movie.title,
    message: props.movie.summary,
    confirmButtonText: '知道了'
  })
}
</script>

<style scoped>
.movie-card {
  background: white;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
}

.poster {
  width: 100%;
  height: 180px;
  overflow: hidden;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.poster img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.info {
  padding: 12px;
}

.title {
  font-size: 14px;
  font-weight: bold;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  color: #333;
}

.meta {
  display: flex;
  justify-content: space-between;
  margin-bottom: 4px;
  font-size: 12px;
}

.rating {
  color: #ff9800;
  font-weight: bold;
}

.year {
  color: #999;
}

.genres {
  font-size: 12px;
  color: #666;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>