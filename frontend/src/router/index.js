import { createRouter, createWebHistory } from 'vue-router'
import PagesOl from '../pages_ol/pages_ol.vue'
import PagesRop from '../pages_rop/pages_rop.vue'
import OlOtchet from '../pages_ol/otchet/otchet.vue' // Путь к файлу корректен

const routes = [
  {
    path: '/pages_ol',
    name: 'PagesOl',
    component: PagesOl
  },
  {
    path: '/pages_ol/otchet',  // Убрал `/otchet.vue` (это не нужно в path!)
    name: 'OlOtchet',
    component: OlOtchet
  },
  {
    path: '/pages_rop',
    name: 'PagesRop',
    component: PagesRop
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router