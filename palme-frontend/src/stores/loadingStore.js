import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useLoadingStore = defineStore('loading', {
  state: () => ({
    isGlobalLoading: ref(false),
    loadingText: ref('加载中...')
  }),

  actions: {
    showLoading(text = '加载中...') {
      this.loadingText = text
      this.isGlobalLoading = true
    },

    hideLoading() {
      this.isGlobalLoading = false
    }
  }
})