<template>
  <div v-if="visible" class="poster-overlay" @click.self="close">
    <div class="poster-container">
      <!-- 海报内容（用于生成图片） -->
      <div
        ref="posterRef"
        class="poster-content"
        :style="{ background: getPosterBackground(result.personality.name) }"
      >
        <!-- 顶部装饰 -->
        <div class="poster-decoration-top">
          <div class="decoration-circle circle-1"></div>
          <div class="decoration-circle circle-2"></div>
          <div class="decoration-circle circle-3"></div>
        </div>

        <!-- 顶部人格区域 -->
        <div class="poster-header">
          <div class="poster-avatar-container">
            <div class="poster-avatar-ring"></div>
            <div class="poster-avatar">
              <img
                :src="result.personality.character_image"
                alt="角色头像"
                @error="handleAvatarError"
              >
            </div>
          </div>

          <div class="poster-badge">
            <span>电影人格</span>
          </div>

          <h2 class="poster-title">{{ result.personality.name }}</h2>
          <p class="poster-subtitle">{{ result.personality.character_name }}</p>
          <p class="poster-movie">《{{ result.personality.movie_name }}》</p>

          <div class="poster-tags">
            <span v-for="(trait, index) in traitsList" :key="index" class="poster-tag">
              {{ trait }}
            </span>
          </div>
        </div>

        <!-- 人格解读 -->
        <div class="poster-interpretation">
          <div class="interpretation-icon">💭</div>
          <p>{{ result.personality.interpretation }}</p>
        </div>

        <!-- 推荐电影 -->
        <div class="poster-movies">
          <div class="poster-section-header">
            <span class="section-icon">🎬</span>
            <h3 class="poster-section-title">为你推荐的电影</h3>
          </div>
          <div class="poster-movies-grid">
            <div v-for="(movie, index) in result.movies.slice(0, 4)" :key="movie.id" class="poster-movie-item">
              <div class="poster-movie-poster">
                <img
                  :src="movie.poster"
                  alt="电影海报"
                  @error="handleMovieError"
                >
                <div class="movie-rating-badge">
                  <span>★</span>
                  <span>{{ movie.douban_rating }}</span>
                </div>
              </div>
              <div class="poster-movie-info">
                <p class="poster-movie-title">{{ movie.title }}</p>
                <p class="poster-movie-genres">{{ movie.genres }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 底部水印 -->
        <div class="poster-footer">
          <div class="footer-logo">
            <span class="logo-text">Palme</span>
          </div>
          <p class="footer-slogan">发现你的电影人格</p>
          <div class="footer-divider"></div>
          <p class="footer-copyright">© 2026 Palme · 扫码开始测试</p>
        </div>

        <!-- 底部装饰 -->
        <div class="poster-decoration-bottom">
          <div class="decoration-wave"></div>
        </div>
      </div>

      <!-- 操作按钮 -->
      <div class="poster-actions">
        <van-button type="default" size="large" class="cancel-btn" @click="close">
          <span class="btn-icon">✕</span>
          取消
        </van-button>
        <van-button
          type="primary"
          size="large"
          class="save-btn"
          :loading="generating"
          @click="generatePoster"
        >
          <span v-if="!generating" class="btn-icon">📷</span>
          {{ generating ? '生成中...' : '保存海报' }}
        </van-button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import html2canvas from 'html2canvas'
import { showToast } from 'vant'

const props = defineProps({
  result: {
    type: Object,
    required: true
  },
  visible: {
    type: Boolean,
    default: false
  }
})

const emit = defineEmits(['update:visible'])

const posterRef = ref(null)
const generating = ref(false)

// 人格特质列表（分割字符串）
const traitsList = computed(() => {
  if (!props.result?.personality?.core_traits) return []
  return props.result.personality.core_traits.split('、').slice(0, 4)
})

// 每个人格专属背景
const getPosterBackground = (name) => {
  const backgrounds = {
    '钢铁侠型': 'linear-gradient(180deg, #1a1a2e 0%, #16213e 30%, #0f3460 60%, #e94560 100%)',
    '千寻型': 'linear-gradient(180deg, #a8edea 0%, #fed6e3 30%, #ffecd2 60%, #fcb69f 100%)',
    '教父型': 'linear-gradient(180deg, #232526 0%, #414345 30%, #1a1a1a 60%, #0d0d0d 100%)',
    '阿甘型': 'linear-gradient(180deg, #f5f7fa 0%, #c3cfe2 30%, #e0eafc 60%, #cfdef3 100%)',
    '赫敏型': 'linear-gradient(180deg, #667eea 0%, #764ba2 30%, #f093fb 60%, #f5576c 100%)',
    '杰克型': 'linear-gradient(180deg, #2c3e50 0%, #4ca1af 30%, #3a6186 60%, #89253e 100%)'
  }
  return backgrounds[name] || 'linear-gradient(180deg, #667eea 0%, #764ba2 50%, #f093fb 100%)'
}

// 图片加载失败处理
const handleAvatarError = (e) => {
  e.target.src = 'https://api.dicebear.com/7.x/avataaars/svg?seed=default'
}

const handleMovieError = (e) => {
  e.target.src = 'https://picsum.photos/seed/movie/300/450'
}

const close = () => {
  emit('update:visible', false)
}

const generatePoster = async () => {
  if (generating.value) return

  generating.value = true
  showToast({
    message: '正在生成海报...',
    icon: 'loading',
    duration: 0
  })

  try {
    // 等待一下确保DOM渲染完成
    await new Promise(resolve => setTimeout(resolve, 300))

    // 生成海报
    const canvas = await html2canvas(posterRef.value, {
      scale: 3, // 3倍超高清
      useCORS: true,
      allowTaint: true,
      backgroundColor: null,
      logging: false,
      imageTimeout: 15000
    })

    // 转换为图片URL
    const imageUrl = canvas.toDataURL('image/jpeg', 0.95)

    // 创建下载链接
    const link = document.createElement('a')
    link.href = imageUrl
    link.download = `Palme-我的电影人格-${props.result.personality.name}-${Date.now()}.jpg`
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)

    showToast({
      message: '海报已保存到相册',
      icon: 'success',
      duration: 2000
    })

    close()
  } catch (error) {
    console.error('生成海报失败:', error)
    showToast({
      message: '生成失败，请重试',
      icon: 'fail',
      duration: 2000
    })
  } finally {
    generating.value = false
  }
}
</script>

<style scoped>
.poster-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.85);
  backdrop-filter: blur(10px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 99999;
  padding: 16px;
  animation: fadeIn 0.3s ease-out;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

.poster-container {
  width: 100%;
  max-width: 380px;
  background: transparent;
  border-radius: 20px;
  overflow: hidden;
  max-height: 92vh;
  display: flex;
  flex-direction: column;
  animation: slideUp 0.4s ease-out;
}

@keyframes slideUp {
  from {
    transform: translateY(30px);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.poster-content {
  width: 100%;
  min-height: 700px;
  padding: 32px 24px;
  color: white;
  position: relative;
  overflow: hidden;
}

/* 装饰元素 */
.poster-decoration-top {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 200px;
  pointer-events: none;
}

.decoration-circle {
  position: absolute;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
}

.circle-1 {
  width: 120px;
  height: 120px;
  top: -40px;
  right: -30px;
}

.circle-2 {
  width: 80px;
  height: 80px;
  top: 60px;
  left: -20px;
}

.circle-3 {
  width: 60px;
  height: 60px;
  top: 120px;
  right: 40px;
}

.poster-decoration-bottom {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 100px;
  pointer-events: none;
}

.decoration-wave {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 60px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 50% 50% 0 0;
}

/* 头部区域 */
.poster-header {
  text-align: center;
  margin-bottom: 28px;
  position: relative;
  z-index: 1;
}

.poster-avatar-container {
  position: relative;
  width: 120px;
  height: 120px;
  margin: 0 auto 20px;
}

.poster-avatar-ring {
  position: absolute;
  top: -4px;
  left: -4px;
  right: -4px;
  bottom: -4px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(255,255,255,0.3), rgba(255,255,255,0.1));
  animation: rotate 8s linear infinite;
}

@keyframes rotate {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}

.poster-avatar {
  position: relative;
  width: 100%;
  height: 100%;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid rgba(255, 255, 255, 0.9);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
              0 0 0 1px rgba(255, 255, 255, 0.2);
}

.poster-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.poster-badge {
  display: inline-block;
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(10px);
  padding: 6px 16px;
  border-radius: 20px;
  font-size: 12px;
  font-weight: 500;
  margin-bottom: 12px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.poster-title {
  font-size: 32px;
  font-weight: 800;
  margin-bottom: 4px;
  text-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
  letter-spacing: 2px;
}

.poster-subtitle {
  font-size: 18px;
  font-weight: 600;
  opacity: 0.95;
  margin-bottom: 4px;
}

.poster-movie {
  font-size: 14px;
  opacity: 0.8;
  margin-bottom: 16px;
  font-style: italic;
}

.poster-tags {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
}

.poster-tag {
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(10px);
  padding: 6px 14px;
  border-radius: 16px;
  font-size: 12px;
  font-weight: 500;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

/* 解读区域 */
.poster-interpretation {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(20px);
  padding: 20px;
  border-radius: 16px;
  margin-bottom: 28px;
  line-height: 1.7;
  font-size: 14px;
  position: relative;
  border: 1px solid rgba(255, 255, 255, 0.15);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.1);
}

.interpretation-icon {
  position: absolute;
  top: -12px;
  left: 20px;
  font-size: 24px;
  background: rgba(255, 255, 255, 0.2);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.poster-interpretation p {
  margin-top: 8px;
}

/* 电影区域 */
.poster-movies {
  margin-bottom: 28px;
  position: relative;
  z-index: 1;
}

.poster-section-header {
  display: flex;
  align-items: center;
  margin-bottom: 16px;
}

.section-icon {
  font-size: 20px;
  margin-right: 8px;
}

.poster-section-title {
  font-size: 16px;
  font-weight: 700;
}

.poster-movies-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 14px;
}

.poster-movie-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-radius: 12px;
  overflow: hidden;
  border: 1px solid rgba(255, 255, 255, 0.15);
  transition: transform 0.3s ease;
}

.poster-movie-poster {
  width: 100%;
  height: 140px;
  overflow: hidden;
  position: relative;
}

.poster-movie-poster img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.movie-rating-badge {
  position: absolute;
  top: 8px;
  right: 8px;
  background: linear-gradient(135deg, #ff9800, #f57c00);
  padding: 4px 8px;
  border-radius: 8px;
  font-size: 11px;
  font-weight: 700;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.3);
}

.poster-movie-info {
  padding: 10px;
}

.poster-movie-title {
  font-size: 13px;
  font-weight: 600;
  margin-bottom: 4px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.poster-movie-genres {
  font-size: 11px;
  opacity: 0.75;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

/* 底部区域 */
.poster-footer {
  text-align: center;
  position: relative;
  z-index: 1;
}

.footer-logo {
  margin-bottom: 8px;
}

.logo-text {
  font-size: 24px;
  font-weight: 800;
  letter-spacing: 4px;
  opacity: 0.9;
}

.footer-slogan {
  font-size: 13px;
  opacity: 0.7;
  margin-bottom: 12px;
}

.footer-divider {
  width: 40px;
  height: 2px;
  background: rgba(255, 255, 255, 0.3);
  margin: 0 auto 12px;
  border-radius: 1px;
}

.footer-copyright {
  font-size: 11px;
  opacity: 0.5;
}

/* 操作按钮 */
.poster-actions {
  display: flex;
  padding: 16px;
  gap: 12px;
  background: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(20px);
}

.cancel-btn {
  flex: 1;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: white;
}

.save-btn {
  flex: 1;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border: none;
  color: white;
}

.btn-icon {
  margin-right: 6px;
}
</style>