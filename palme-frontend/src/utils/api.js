import axios from 'axios'
import { showToast } from 'vant'

const api = axios.create({
  baseURL: '/api',
  timeout: 15000
})

// 请求拦截器
api.interceptors.request.use(
  (config) => {
    // 不要在顶层导入store，在拦截器内部动态获取
    // 这样可以确保Pinia已经初始化
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// 响应拦截器 - 添加自动重试
api.interceptors.response.use(
  (response) => {
    return response
  },
  async (error) => {
    const config = error.config
    if (!config || !config.retry) {
      config.retry = 3 // 默认重试3次
      config.retryDelay = 1000 // 重试间隔1秒
    }

    // 检查是否还有重试次数
    if (config.retry > 0) {
      config.retry--
      showToast(`网络请求失败，正在重试... (${3 - config.retry}/3)`)

      // 等待后重试
      await new Promise(resolve => setTimeout(resolve, config.retryDelay))
      return api(config)
    }

    showToast('网络请求失败，请检查网络连接')
    return Promise.reject(error)
  }
)

// 创建会话
export const createSession = () => api.post('/sessions/create_session/')

// 获取所有问题
export const getQuestions = () => api.get('/questions/')

// 提交所有答案
export const submitAllAnswers = (data) => api.post('/answers/submit_all_answers/', data)

// 根据会话ID获取结果
export const getResultBySession = (sessionId) => api.get(`/results/get_by_session/?session_id=${sessionId}`)

export default api