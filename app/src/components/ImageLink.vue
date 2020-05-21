<template>
  <router-link :to="{ name: 'image-detail', params: { id: image.id }}">
    <img v-bind:src="image.url" />
  </router-link>
</template>

<script>
export default {
  name: 'ImageLink',
  props: {
    image: { type: Object },
  },
};
</script>

<style scoped>
  a {
    margin-top: 8px;
    vertical-align: middle;
    width: 100%;
  }
  a img {
    width: 100%;
  }
</style>
