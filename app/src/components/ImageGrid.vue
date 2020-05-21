<template>
  <div class="image-grid">
    <div class="column">
      <div class="sub-column">
        <image-link
          :image="image"
          v-for="image in firstColumn"
          :key="image.id"
        ></image-link>
      </div>
      <div class="sub-column">
        <image-link
          :image="image"
          v-for="image in secondColumn"
          :key="image.id"
        ></image-link>
      </div>
    </div>
    <div class="column">
      <div class="sub-column">
        <image-link
          :image="image"
          v-for="image in thirdColumn"
          :key="image.id"
        ></image-link>
      </div>
      <div class="sub-column">
        <image-link
          :image="image"
          v-for="image in fourthColumn"
          :key="image.id"
        ></image-link>
      </div>
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
  }
  a {
    display: inline-flex;
  }
  .column {
    display: flex;
    flex: calc(50%);
    flex-flow: wrap;
    max-width: calc(50%);
    padding: 0;
  }
  .sub-column {
    flex: calc(50% - 8px);
    max-width: calc(50% - 8px);
    margin: 0 4px;
  }

  /* Responsive layout */
  @media screen and (max-width: 800px) {
    .column {
      display: block;
    }
    .sub-column {
      max-width: calc(100% - 8px);
    }
  }

  @media screen and (max-width: 600px) {
    .image-grid {
      display: block;
    }
    .column {
      max-width: 100%;
    }
  }
</style>
