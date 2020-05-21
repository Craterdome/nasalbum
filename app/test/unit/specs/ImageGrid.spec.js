import Vue from 'vue';
import ImageGrid from '@/components/ImageGrid';

describe('ImageGrid.vue', () => {
  it('should have a style class', () => {
    const Constructor = Vue.extend(ImageGrid);
    const vm = new Constructor().$mount();
    expect(vm.$el.classList.contains('image-grid'));
  });
});
