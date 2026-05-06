<template>
  <router-view v-slot="{ Component, route }">
    <transition :name="route.meta.transition || 'fade'" mode="out-in">
      <component :is="Component"/>
    </transition>
  </router-view>

  <!-- 全局加载指示器 -->
  <van-overlay :show="loadingStore.isGlobalLoading" z-index="9999">
    <div class="global-loading">
      <van-loading size="large" vertical>
        {{ loadingStore.loadingText }}
      </van-loading>
    </div>
  </van-overlay>
</template>

<script setup>
import {useLoadingStore} from './stores/loadingStore'

const loadingStore = useLoadingStore()
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html, body, #app {
  width: 100%;
  height: 100%;
  overflow: hidden;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  /* 安全区域适配 */
  padding-bottom: env(safe-area-inset-bottom);
}

/* 隐藏滚动条 */
::-webkit-scrollbar {
  display: none;
}

/* 页面过渡动画 */
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}

.slide-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.slide-leave-to {
  transform: translateX(-100%);
  opacity: 0;
}

/* 全局加载样式 */
.global-loading {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: white;
  z-index: 10000;
}
</style>