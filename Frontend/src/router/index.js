
import Vue from 'vue'
import VueRouter from 'vue-router'
import RegisterUser from '../components/RegisterUser.vue'
import LoginUser from '../components/LoginUser.vue'
import HomePage from '../components/HomePage.vue'
import DashBoard from '../views/DashBoard.vue'
import CreateBlog from '../components/CreateBlog.vue'
import UserProfile from '../views/UserProfile.vue'

import OtherProfile from '../views/OtherProfile.vue'
Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        name: 'homepage',
        component : HomePage
    },

    {
        path: '/login',
        name: 'login',
        component: LoginUser
    },

    {
        path: '/register',
        name: 'register',
        component: RegisterUser
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: DashBoard
    },

    {
        path: '/createblog',
        name: 'createblog',
        component: CreateBlog
    },
    {
        path: '/userprofile',
        name: 'userprofile',
        component: UserProfile
    },
    
    {
        path: '/otherprofile/:username',
        name: 'otherprofile',
        component: OtherProfile
    }
    
]
const router = new VueRouter({
    routes})
export default router
