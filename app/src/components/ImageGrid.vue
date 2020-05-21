<template>
  <div class="image-grid">
    <router-link
      :to="{ name: 'image-detail', params: { id: image.nasaId }}"
      v-for="image in images" :key="image.url"
    >
      <img v-bind:src="image.url" />
    </router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Album',
  data() {
    return {
      images: [],
    };
  },
  mounted() {
    axios.get('/api/images.json').then((response) => {
      this.images = response.data;
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .image-grid {
    display: flex;
    flex-wrap: wrap;
    padding: 0 4px;
  }
  a {
    flex: 8px;
    vertical-align: middle;
    width: 100%;
  }
  a img {
    margin-top: 8px;
    vertical-align: middle;
    width: 100%;
  }
</style>
