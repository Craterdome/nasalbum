<template>
  <div id="app">
    <router-link to="/">
      <img class="logo" src="./assets/nasaLogo-570x450.png">
    </router-link>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
  body {
    margin: 8px 4px;
  }
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  img.logo {
    max-width: 150px;
  }
</style>
