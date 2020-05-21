<template>
  <div>
    <img :src="image.url"/>
    <div class="container" v-if="prevImage || nextImage">
      <router-link
        v-if="prevImage.id"
        :to="{ name: 'image-detail', params: { id: prevImage.id }}"
        style="text-align: left"
      >
        &laquo; Previous image
      </router-link>
      <router-link
        v-if="nextImage.id"
        :to="{ name: 'image-detail', params: { id: nextImage.id }}"
        style="text-align: right"
      >
        Next image &raquo;
      </router-link>
    </div>
    <div class="image-metadata container">
      <div v-if="image.album">
        <strong>Album: </strong>{{ image.album }}
      </div>
      <div v-if="image.center">
        <strong>Center: </strong>{{ image.center }}
      </div>
      <div v-if="image.creator">
        <strong>Creator: </strong>{{ image.creator }}
      </div>
      <div v-if="image.dateCreated">
        <strong>Date: </strong>{{ image.dateCreated }}
      </div>
    </div>
    <p class="container" v-html="image.description"></p>
    <div v-if="keywords" class="image-keywords container">
      <strong>Keywords:</strong> {{ keywords }}
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Album',
  data() {
    return {
      image: {},
      nextImage: {},
      prevImage: {},
    };
  },
  computed: {
    keywords() {
      if (this.image && this.image.keywords) {
        return this.image.keywords.join(', ');
      }
      return '';
    },
  },
  created() {
    this.fetchData();
  },
  watch: {
    // call again the method if the route changes
    $route: 'fetchData',
  },
  methods: {
    fetchData() {
      axios.get('/api/images.json').then((response) => {
        response.data.forEach((image, index) => {
          if (image.id.toString() === this.$route.params.id.toString()) {
            this.image = image;
            if (response.data.length > index + 1) {
              this.nextImage = response.data[index + 1];
            } else {
              this.nextImage = {};
            }
            if (index > 0) {
              this.prevImage = response.data[index - 1];
            } else {
              this.prevImage = {};
            }
          }
        });
      });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  img {
    max-width: 100%;
    margin-bottom: 0;
  }
  .image-metadata {
    display: flex;
    font-size: .8rem;
  }
  .image-metadata div {
    flex: 1;
  }
  p {
    font-size: .9rem;
    text-align: left;
  }
  .image-keywords {
    color: #444;
    font-size: .7rem;
    margin: 1rem;
  }
  a {
    color: #1f69c0;
    display: inline-block;
    font-size: .8rem;
    padding: .2rem 0 1rem;
    text-decoration: none;
    width: calc(50% - 4px);
  }
  .container {
    margin-left: auto;
    margin-right: auto;
    max-width: 800px;
  }
  p.container {
    margin: 1rem auto;
  }
</style>
