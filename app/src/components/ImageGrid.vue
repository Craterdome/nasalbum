<template>
  <div class="image-grid">
    <div class="column">
      <image-link
        :image="image"
        v-for="image in firstColumn"
        :key="image.url"
      ></image-link>
    </div>
    <div class="column">
      <image-link
        :image="image"
        v-for="image in secondColumn"
        :key="image.url"
      ></image-link>
    </div>
    <div class="column">
      <image-link
        :image="image"
        v-for="image in thirdColumn"
        :key="image.url"
      ></image-link>
    </div>
    <div class="column">
      <image-link
        :image="image"
        v-for="image in fourthColumn"
        :key="image.url"
      ></image-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import ImageLink from '@/components/ImageLink';

export default {
  name: 'Album',
  components: { ImageLink },
  data() {
    return {
      images: [],
    };
  },
  computed: {
    // divide our images into 4 columns for design reasons
    firstColumn() {
      return this.images.filter((image, index) => (index + 4) % 4 === 0);
    },
    secondColumn() {
      return this.images.filter((image, index) => (index + 3) % 4 === 0);
    },
    thirdColumn() {
      return this.images.filter((image, index) => (index + 2) % 4 === 0);
    },
    fourthColumn() {
      return this.images.filter((image, index) => (index + 1) % 4 === 0);
    },
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
  .column {
    flex: 25%;
    max-width: calc(25% - 4px);
    padding: 0 2px;
  }

  /* Responsive layout */
  @media screen and (max-width: 800px) {
    .column {
      flex: calc(50% - 4px);
      max-width: calc(50% - 4px);
    }
  }

  @media screen and (max-width: 600px) {
    .column {
      flex: 100%;
      max-width: 100%;
    }
  }
</style>
