<template>
  <div id="app">
    <nav>
      <router-link to="/pages_ol">Переход на Pages OL</router-link> |
      <router-link to="/pages_rop">Переход на Pages ROP</router-link>
    </nav>
    
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
nav {
  padding: 20px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 0 10px;
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>