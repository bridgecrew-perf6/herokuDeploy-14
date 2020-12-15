import { createWebHistory, createRouter } from 'vue-router'
import Login from './components/Login'
import Register from './components/Register'
import App from './App'

const routes = [{
        path: '/',
        name: "root",
        component: App
    }, {
        path: '/user/login',
        name: "login",
        component: Login
    }, {
        path: '/user/register',
        name: "register",
        component: Register
}]
const router = new createRouter({
    history: createWebHistory(),
    routes
})
export default router