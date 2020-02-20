import Vue from 'vue';
import Router from 'vue-router';
// const HeaderParts = () => import (/* webpackChunkName: "HeaderParts" */'./components/HeaderParts.vue');
// const SideMenu = () => import (/* webpackChunkName: "SideMenu" */'./views/SideMenu.vue');
const Top = () => import (/* webpackChunkName: "Top/" */'./views/Top.vue');
const About = () => import (/* webpackChunkName: "About" */'./views/About.vue');
const MySelf = () => import (/* webpackChunkName: "MySelf" */'./views/MySelf.vue');
const Works= () => import (/* webpackChunkName: "Works" */'./views/Works.vue');
const Contact = () => import (/* webpackChunkName: "Contact" */'./views/Contact.vue');
const Environment = () => import (/* webpackChunkName: "Environment" */'./views/Environment.vue');

Vue.use(Router);



export default new Router({
    mode: "history",
    routes: [
        {
            path:'/',
            components: {
                default: Top,
                header: Top,
                name: top
            },
        },
        {
            path: '/about',
            components: {
                default: About,
                header: About,
            },
        },
        {
            path: '/myself',
            components:{
                default: MySelf,
                header: MySelf,
            },
        },
        {
            path: '/works',
            components:{
                default: Works,
                header: Works,
            },
        },
        {
            path: '/contact',
            components:{
                default: Contact,
                header: Contact,
            },
        },
        {
            path: '/Environment',
            components: {
                default: Environment,
                header: Environment
            },
        },
    ],
})