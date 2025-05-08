// create-vue-structure.js
const fs = require('fs');
const path = require('path');

// Структура папок и файлов
const structure = [
  {
    dir: 'pages_ol',
    file: 'pages_ol.vue',
    content: `<template>
  <div>
    <!-- Содержимое компонента pages_ol -->
  </div>
</template>

<script>
export default {
  name: 'PagesOl',
  // Логика компонента
}
</script>

<style scoped>
/* Стили компонента */
</style>`
  },
  {
    dir: 'pages_rop',
    file: 'pages_rop.vue',
    content: `<template>
  <div>
    <!-- Содержимое компонента pages_rop -->
  </div>
</template>

<script>
export default {
  name: 'PagesRop',
  // Логика компонента
}
</script>

<style scoped>
/* Стили компонента */
</style>`
  }
];

// Создаем папки и файлы
structure.forEach(({ dir, file, content }) => {
  const dirPath = path.join(__dirname, dir);
  const filePath = path.join(dirPath, file);
  
  // Создаем папку, если ее нет
  if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
  }
  
  // Создаем файл, если его нет
  if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, content);
    console.log(`Создан файл: ${dir}/${file}`);
  } else {
    console.log(`Файл уже существует: ${dir}/${file}`);
  }
});

console.log('Структура создана!');
