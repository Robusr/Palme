import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 10000
})

// 创建会话
export const createSession = () => api.post('/sessions/create_session/')

// 获取所有问题
export const getQuestions = () => api.get('/questions/')

// 提交所有答案
export const submitAllAnswers = (data) => api.post('/answers/submit_all_answers/', data)

// 根据会话ID获取结果
export const getResultBySession = (sessionId) => api.get(`/results/get_by_session/?session_id=${sessionId}`)

export default api