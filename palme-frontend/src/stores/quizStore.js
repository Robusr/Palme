import {defineStore} from 'pinia'
import {ref, computed} from 'vue' // 添加这行！
import {createSession, getQuestions, submitAllAnswers, getResultBySession} from '../utils/api'

export const useQuizStore = defineStore('quiz', {
    state: () => ({
        sessionId: null,
        questions: [],
        currentQuestionIndex: 0,
        answers: [],
        result: null,
        loading: false
    }),

    actions: {
        // 初始化：创建会话并获取问题
        async initQuiz() {
            this.loading = true
            try {
                const sessionRes = await createSession()
                this.sessionId = sessionRes.data.session_id

                const questionsRes = await getQuestions()
                this.questions = questionsRes.data

                this.currentQuestionIndex = 0
                this.answers = []
                this.result = null
            } catch (error) {
                console.error('初始化失败:', error)
            } finally {
                this.loading = false
            }
        },

        // 提交答案并进入下一题
        submitAnswer(optionId) {
            const currentQuestion = this.questions[this.currentQuestionIndex]
            this.answers.push({
                question_id: currentQuestion.id,
                option_id: optionId
            })

            if (this.currentQuestionIndex < this.questions.length - 1) {
                this.currentQuestionIndex++
            }
        },

        // 提交所有答案并获取结果
        async submitAllAnswers() {
            this.loading = true
            try {
                const res = await submitAllAnswers({
                    session_id: this.sessionId,
                    answers: this.answers
                })
                this.result = res.data
                return res.data
            } catch (error) {
                console.error('提交答案失败:', error)
            } finally {
                this.loading = false
            }
        },


        resetQuiz() {
            this.sessionId = null
            this.questions = []
            this.currentQuestionIndex = 0
            this.answers = [] // 确保重置answers数组
            this.result = null
        }
    }
})