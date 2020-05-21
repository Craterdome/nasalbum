import Vue from 'vue';
import Router from 'vue-router';
import ImageDetail from '@/components/ImageDetail';
import ImageGrid from '@/components/ImageGrid';

Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'image-grid',
      component: ImageGrid,
    },
    {
      path: '/image/:id/',
      name: 'image-detail',
      component: ImageDetail,
    },
  ],
});
