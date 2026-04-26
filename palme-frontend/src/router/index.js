import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Quiz from '../pages/Quiz.vue'
import Result from '../pages/Result.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: { transition: 'fade' }
  },
  {
    path: '/quiz',
    name: 'Quiz',
    component: Quiz,
    meta: { transition: 'slide' }
  },
  {
    path: '/result',
    name: 'Result',
    component: Result,
    meta: { transition: 'fade' }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router