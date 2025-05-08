<template>

  <div class="cont">
    <div class="sokr">
      <center>
        <div class="serif d-flex flex-column mx-auto" style="width: 98%;">
          <!--Расположение элементов сверху вниз -->
          <!-- Описнаие заголовка -->
          <div style="text-align: left;">
            <h2><b> Главная страница </b></h2>
          </div>
          <div class="color_block">
            <div style="text-align: left;">
              <h2> Объявления </h2>
            </div>
            <div class="BLOCK2">
              <div id="FILTR" class="footer">Фильтр</div>
              <div class="footer"><button class="KNOPKA">Применить</button></div>
              <div class="d-flex flex-column">
                <label for="start">Дата от:</label>
                <input type="date" id="start" name="trip-start" value="2018-07-22" min="2018-01-01" max="2030-12-31" />
              </div>
              <div class="d-flex flex-column" style="flex-grow: 1;">
                <label for="start">Объявление</label>
                <input id="vvod" type="text" placeholder="Введите текст">
              </div>
            </div>
            <!-- ТАблица -->
            <div class="BLOCK23 scroll-table">
              <table>
                <colgroup>
                  <col style="width: 100px;"> <!-- 1 часть -->
                  <col style="width: 100%;"> <!-- 5 частей -->
                </colgroup>
                <thead>
                  <tr>
                    <th class="col">Дата</th>
                    <th class="col">Объявление</th>
                  </tr>
                </thead>
              </table>
              <div class="shok scroll-table-body">
                <table>
                  <colgroup>
                    <col style="width: 100px;"> <!-- 1 часть -->
                    <col style="width: 100%;"> <!-- 5 частей -->
                  </colgroup>
                  <tbody>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                    <tr>
                      <td>12.03.2024</td>
                      <td>Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023 вступают в
                        силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением лицензионных
                        условий. Сообщаем о внесении изменений в требования к лицензированию по ОПК 4. С 01.12.2023
                        вступают в силу новые нормативные акты, касающиеся отчетности и контроля за соблюдением
                        лицензионных условий. </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
          <div class="color_block Block3">
            <div>
              <div style="text-align: left;">
                <h2> Мои ООП </h2>
              </div>
              <div class="BLOCK4">
                <div id="FILTR" class="footer">Фильтр</div>
                <div class="footer"><button class="KNOPKA">Применить</button></div>
                <div class="d-flex flex-column">
                  <label for="year">Год набора</label>
                  <select id="year" name="year">
                    <option value="2025">2025</option>
                    <option value="2024">2024</option>
                    <option value="2023">2023</option>
                  </select>
                </div>
                <div class="d-flex flex-column flex-grow-3">
                  <label for="code">Шифр</label>
                  <input id="code" type="text" placeholder="Введите текст">
                </div>
                <div class="d-flex flex-column flex-grow-1">
                  <label for="name">Наименование</label>
                  <input id="name" type="text" placeholder="Введите текст">
                </div>
              </div>
            </div>
            <div class="Block33">
              <!-- ТАБЛИЦА -->
              <table>
                <colgroup>
                  <col style="width: 90px;"> <!-- 1 часть -->
                  <col style="width: 40%;"> <!-- 5 частей -->
                  <col style="width: 250px;"> <!-- 1 часть -->
                  <col style="width: 100px;"> <!-- 1 часть -->
                </colgroup>
                <thead>
                  <tr>
                    <th class="col">Год набора</th>
                    <th class="col">Шифр и наименование</th>
                    <th class="col">Файлы и их статус</th>
                    <th class="col">Статус ОП</th>
                  </tr>
                </thead>
              </table>
              <div class="vniz scroll-table-body">
                <table id="myTable">
                  <colgroup>
                    <col style="width: 90px;"> <!-- 1 часть -->
                    <col style="width: 40%;"> <!-- 5 частей -->
                    <col style="width: 250px;"> <!-- 1 часть -->
                    <col style="width: 100px;"> <!-- 1 часть -->
                  </colgroup>
                  <tbody>
                    <tr class="clickable-row" @click="toggleBlock('block-2')">
  <td>2022</td>
  <td>09.03.02 - Информационные системы и технологии.</td>
  <td class="status-cell">
    Паспорт - Отсутствует<br>
    Схема - Отсутствует<br>
    Матрица - на доработке
  </td>
  <td class="status-cell">не сдана</td>
</tr>
<tr class="clickable-row" @click="toggleBlock('block-2')">
  <td>2023</td>
  <td>09.03.02 - Информационные системы и технологии.</td>
  <td class="status-cell">
    Паспорт - Отсутствует<br>
    Схема - Отсутствует<br>
    Матрица - на доработке
  </td>
  <td class="status-cell">не сдана</td>
</tr>
<tr class="clickable-row" @click="toggleBlock('block-2')">
  <td>2025</td>
  <td>09.03.02 - Информационные системы и технологии.</td>
  <td class="status-cell">
    Паспорт - Отсутствует<br>
    Схема - Отсутствует<br>
    Матрица - на доработке
  </td>
  <td class="status-cell">не сдана</td>
</tr>
<tr class="clickable-row" @click="toggleBlock('block-2')">
  <td>2025</td>
  <td>09.03.02 - Информационные системы и технологии.</td>
  <td class="status-cell">
    Паспорт - Отсутствует<br>
    Схема - Отсутствует<br>
    Матрица - на доработке
  </td>
  <td class="status-cell">не сдана</td>
</tr>

                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </div>
      </center>
    </div>

    <div  id="block-2" class="hidden-block">
      <!-- style="display: none; Это для верхнего Div -->
<!-- #Тут начало -->
<div class="serif d-flex flex-column mx-auto" style="width: 98%;"> <!--Расположение элементов сверху вниз -->
    <!-- Описнаие заголовка -->
    <div style="text-align: left;">   
        <h3><b>
           <!-- <div class="badge text-bg-info" id="toggleButton">Главная страница/</div> -->

            <div id="toggleButtonN" class="Zag2-1">  09. 03.02 - 2025 -Информационные системы и технологии ИСиТ</div></b></h3>
    </div>

    <div class="color_block">
        <div style="text-align: left;">

        <!-- ТАблица -->
        <div  class="">
            <table>
                <colgroup>
                    <col style="width: 100px;"> <!-- 1 часть -->
                    <col style="width: 100px;"> <!-- 2 частей -->
                    <col style="width: 130px;"> <!-- 3 частей -->
                    <col style="width: 100px;"> <!-- 4 частей -->
                    <col style="width: 100%;" class="min-width"> <!-- 5 частей -->
                </colgroup>
                <thead>
                    <tr>
                        <th class="col">Документ</th>
                        <th class="col">Статус</th>
                        <th class="col">Загруженный докмуент</th>
                        <th class="col">Дата загрузки РОПом</th>
                        <th class="col">История сообщений</th>
                    </tr>
                </thead>
            </table>
            <div class="shok2 scroll-table-body">
                <table>
                    <colgroup>
                        <col style="width: 100px;"> <!-- 1 часть -->
                        <col style="width: 100px;"> <!-- 2 частей -->
                        <col style="width: 130px;"> <!-- 3 частей -->
                        <col style="width: 100px;"> <!-- 4 частей -->
                        <col style="width: 100%;" class="min-width"> <!-- 5 частей -->
                    </colgroup>
                    <tbody>
                      <tr>
                        <td>Паспорт</td>
                        <td class="status-cell">принят</td>
                        <td><a href="Ссылка">
                            Скачать 
                        </a>
                        <a href="Ссылка"> 
                            Загрузить </a> </td>
                        <td>16.03.2024</td>
                        <!-- Бублик -->
                        <td class="scrollR">
                            <br>
                            16.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Принято
                            <br>  
                            <br>
                            <br>  
                            15.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                            <br>  
                            15.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                            <br>  
                            14.03.2025:
                            <br>
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                        </td>
                    </tr>
                    <tr>
                        <td>Матрица</td>
                        <td class="status-cell">на доработке</td>
                        <td><a href="Ссылка">
                            Загрузить 
                        </a> </td>
                        <td>12.03.2024</td>
                        <!-- Бублик -->
                        <td class="scrollR">
                            <br>
                            16.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу
                            <br>  
                            <br>
                            <br>  
                            15.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                            <br>  
                            15.03.2025:
                            <br>  
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                            <br>  
                            14.03.2025:
                            <a href="Ссылка">
                                Скачать предыдущую версию файла 
                            </a>
                            <br>
                            Не соответствует приказу ректора №267-О от  20.02.25.
                            <br>  
                        </td>
                    </tr>
                    <tr>
                        <td>Схема</td>
                        <td class="status-cell">Отсутствует</td>
                        <td><a href="Ссылка">
                            Загрузить 
                        </a> </td>
                        <td>12.03.2024</td>
                        <!-- Бублик -->
                        <td class="scrollR">

                        </td>
                    </tr>


                    </tbody>



                  </table>
                </div>
          </div>
</div>
  </div>

  </div>
</div>
  </div>


</template>

<script>
import './script.js'; // Путь верный, если файл в той же папке

export default {
  name: 'PagesRop',
  mounted() {
    console.log("Скрипт подключён!");
    this.highlightKeywordsInCells();
  },
  methods: {
    highlightKeywordsInCells() {
      // Находим все ячейки с классом "status-cell"
      const statusCells = document.querySelectorAll(".status-cell");

      // Ключевые слова и их классы
      const keywords = [
        // { text: "не принята", className: "red" },
        { text: "принята", className: "badge text-bg-success" },
        // { text: "не принят", className: "red" },
        { text: "принят", className: "badge text-bg-success" },
        { text: "отсутствует", className: "badge text-bg-danger" },
        { text: "на доработке", className: "badge text-bg-warning" },
        { text: "не сдана", className: "badge text-bg-danger" },
        { text: "Сдана", className: "badge text-bg-success" }
      ];

      // Функция для оборачивания ключевых слов в <span>
      const highlightKeywords = (cell) => {
        let html = cell.innerHTML; // Получаем HTML-содержимое ячейки

        // Проходим по каждому ключевому слову
        keywords.forEach(keyword => {
          // Создаём регулярное выражение с учётом пробелов и переносов строк
          const regex = new RegExp(`(\\s|^)${keyword.text}(\\s|$|<br>)`, "gi");
          // Заменяем ключевые слова на <span> с классом
          html = html.replace(regex, `$1<span class="${keyword.className}">${keyword.text}</span>$2`);
        });

        cell.innerHTML = html; // Обновляем содержимое ячейки
      };

      // Применяем функцию к каждой ячейке
      statusCells.forEach(highlightKeywords);
    }
  }
}
</script>


<style>
/* Импорт всего CSS-файла */
@import url('./style.css');
</style>