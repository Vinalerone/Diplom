document.addEventListener('DOMContentLoaded', function() {
  // Элементы управления
  const toggleButton = document.getElementById('toggleButton');
  const statusCells = document.querySelectorAll(".status-cell");
  const clickableRows = document.querySelectorAll('.clickable-row');

  // Ключевые слова
  const keywords = [
      { text: "принята", className: "badge text-bg-success" },
      { text: "сдан", className: "badge text-bg-success" },
      { text: "принят", className: "badge text-bg-success" },
      { text: "отсутствует", className: "badge text-bg-danger" },
      { text: "на доработке", className: "badge text-bg-warning" },
      { text: "не_сдана", className: "badge text-bg-danger" },
      { text: "не_сдан", className: "badge text-bg-danger" },
      { text: "Сдана", className: "badge text-bg-success" }
  ];

  // Подсветка ключевых слов
  function highlightKeywords(cell) {
      let html = cell.innerHTML;
      
      keywords.forEach(keyword => {
          const escapedText = keyword.text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
          const regex = new RegExp(`(\\s|^)${escapedText}(\\s|$|<br>)`, "gi");
          html = html.replace(regex, `$1<span class="${keyword.className}">${keyword.text}</span>$2`);
      });

      cell.innerHTML = html;
  }

  // Обработчики событий
  function setupEventListeners() {
      // Подсветка статусов
      if (statusCells.length) {
          statusCells.forEach(highlightKeywords);
      }

      // Клики по строкам
      if (clickableRows.length) {
          clickableRows.forEach(row => {
              row.addEventListener('click', () => {
                  const targetId = row.getAttribute('data-target');
                  const block = document.getElementById(targetId);
                  if (block) {
                      block.style.display = block.style.display === 'none' ? 'block' : 'none';
                      checkWidthAndBlockVisibility();
                  }
              });
          });
      }

      // Кнопка переключения
      if (toggleButton) {
          toggleButton.addEventListener('click', function() {
              const block = document.getElementById('block-2');
              if (block) {
                  block.style.display = block.style.display === 'none' ? 'block' : 'none';
                  checkWidthAndBlockVisibility();
              }
          });
      }
  }

  // Проверка ширины окна
  function checkWidthAndBlockVisibility() {
      const block2 = document.getElementById('block-2');
      const sokrDiv = document.querySelector('.sokr');
      
      if (block2 && sokrDiv) {
          const isBlock2Visible = block2.style.display !== 'none';
          const isWindowNarrow = window.innerWidth < 1000;

          sokrDiv.style.display = (isBlock2Visible && isWindowNarrow) ? 'none' : '';
      }
  }

  // Инициализация
  setupEventListeners();
  checkWidthAndBlockVisibility();
  
  // Реакция на изменение размера окна
  window.addEventListener('resize', checkWidthAndBlockVisibility);
});

// Отсюда удалять

function handleToggleButtonVisibility() {
  const toggleButton = document.getElementById('toggleButton');
  if (!toggleButton) return;
  
  if (window.innerWidth > 1000) {
      toggleButton.style.display = 'none';
  } else {
      toggleButton.style.display = ''; // Восстанавливаем исходное значение
  }
}

// Первоначальная проверка
window.addEventListener('DOMContentLoaded', handleToggleButtonVisibility);

// Проверка при изменении размера окна
window.addEventListener('resize', handleToggleButtonVisibility);