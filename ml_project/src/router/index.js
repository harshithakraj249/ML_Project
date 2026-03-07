import Vue from 'vue'
import VueRouter from 'vue-router'
import Dashboard from '../views/Dashboard.vue'
import Projects from '../views/Projects.vue'
import Facerecognition from '../views/FaceRecognition.vue'
import Sentiment from '../views/Sentiment.vue'
import Ocr from '../views/Ocr.vue'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'dashborad',
        component: Dashboard
    },
    {
        path: '/projects',
        name: 'projects',
        component: Projects,
        children: [
            { path: '/projects/face', component: Facerecognition },
            { path: '/projects/sentiment', component: Sentiment },
            { path: '/projects/ocr', component: Ocr }
        ]
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router