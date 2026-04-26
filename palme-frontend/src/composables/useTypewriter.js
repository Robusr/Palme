import { ref, watch } from 'vue'

export function useTypewriter(text, speed = 40) {
  const displayedText = ref('')
  const isTyping = ref(false)
  let timer = null

  const type = async (newText) => {
    // 清除之前的定时器
    if (timer) {
      clearTimeout(timer)
      timer = null
    }

    isTyping.value = true
    displayedText.value = ''

    for (let i = 0; i < newText.length; i++) {
      displayedText.value += newText[i]
      await new Promise(resolve => {
        timer = setTimeout(resolve, speed)
      })
    }

    isTyping.value = false
  }

  // 只在text真正变化时才重新打字
  watch(text, (newText) => {
    if (newText) {
      type(newText)
    }
  }, { immediate: true, deep: false })

  return {
    displayedText,
    isTyping
  }
}