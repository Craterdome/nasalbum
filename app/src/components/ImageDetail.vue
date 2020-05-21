<template>
  <div>
    <img :src="image.url"/>
    <div class="image-metadata">
      <div>
        <strong>Album: </strong>{{ image.album }}
      </div>
      <div>
        <strong>Center: </strong>{{ image.center }}
      </div>
      <div>
        <strong>Creator: </strong>{{ image.creator }}
      </div>
      <div><strong>Date: </strong>{{ image.dateCreated }}
      </div>
    </div>
    <p v-html="image.description"></p>
    <div class="image-keywords"><strong>Keywords:</strong> {{ keywords }}</div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Album',
  data() {
    return {
      image: {},
    };
  },
  computed: {
    keywords() {
      if (this.image) {
        return this.image.keywords.join(', ');
      }
      return '';
    },
  },
  mounted() {
    axios.get('/api/images.json').then((response) => {
      this.image = response.data.find(image => image.nasaId === this.$route.params.id);
    });
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  img {
    max-width: 100%;
    margin-bottom: 1rem;
  }
  .image-metadata {
    display: flex;
    font-size: .8rem;
  }
  .image-metadata div {
    flex: 8px;
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
</style>
