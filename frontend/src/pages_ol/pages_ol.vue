<template>
  <div>
    <nav>
      <div id="app">
        <Div class="Color-block">
          <router-link to="/pages_ol/analiz"> <h2 class="ZagMenu"> Меню</h2></router-link>
        </Div>
      <div class="Color-block">
        <div class="buttons-container">
          <router-link to="/pages_ol/main_ol" class="btn btn-outline-primary">Экспертиза</router-link>
          <router-link to="/pages_ol/news" class="btn btn-outline-primary">Объявления</router-link>
          <router-link to="/pages_ol/otchet" class="btn btn-outline-primary">Отчёты</router-link>
        </div>
      </div>
    </div>
    </nav>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'pages_ol'
}
</script>

<style>
/* Импорт всего CSS-файла */
@import url('./Wstyle.css');


</style>