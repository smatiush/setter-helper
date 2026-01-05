// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router';
import WallsPage from '@/components/WallsPage.vue';
import RoutesPage from '@/components/RoutesPage.vue';
import ExplorePage from '@/components/ExplorePage.vue';

const routes = [
  { path: '/walls', name: 'Walls', component: WallsPage },
  { path: '/routes', name: 'Routes', component: RoutesPage },
  { path: '/explore', name: 'Explore', component: ExplorePage },
  { path: '/:pathMatch(.*)*', redirect: '/walls' }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
