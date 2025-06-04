document.addEventListener('DOMContentLoaded', function() {
    const input = document.getElementById('svvod');  // Исправлено на svvod
    const measurer = document.getElementById('smeasurer');  // Исправлено на smeasurer

    function updateInputWidth() {
        // Берем текст из input или placeholder, если поле пустое
        const text = input.value || input.placeholder;
        
        // Записываем текст в измеритель
        measurer.textContent = text;
        
        // Вычисляем ширину текста (+ отступы)
        const textWidth = measurer.offsetWidth;
        
        // Устанавливаем новую ширину (но не меньше 200px)
        input.style.width = Math.max(200, textWidth) + 'px';
    }

    // Обновляем ширину при:
    input.addEventListener('input', updateInputWidth);  // Ввод текста
    input.addEventListener('focus', updateInputWidth);  // Фокусе
    input.addEventListener('blur', updateInputWidth);   // Потере фокуса

    // Инициализация при загрузке
    updateInputWidth();
});

// Для цвета

// Другой ккод тут
// Находим все ячейки с классом "status-cell"
const statusCells = document.querySelectorAll(".status-cell");

// Ключевые слова и их классы
const keywords = [
   // { text: "не принята", className: "red" },
    { text: "принята", className: "badge text-bg-success" },
   // { text: "не принят", className: "red" },
    { text: "принят", className: "badge text-bg-success" },
   // { text: "отсутствует", className: "badge text-bg-danger" },
    { text: "на доработке", className: "badge text-bg-warning" },
    { text: "не сдана", className: "badge text-bg-danger" },
    { text: "Сдана", className: "badge text-bg-success" },
    { text: "не_проверено", className: "badge text-bg-danger" }
];

// Функция для оборачивания ключевых слов в <span>
function highlightKeywords(cell) {
    let html = cell.innerHTML; // Получаем HTML-содержимое ячейки

    // Проходим по каждому ключевому слову
    keywords.forEach(keyword => {
        // Создаём регулярное выражение с учётом пробелов и переносов строк
        const regex = new RegExp(`(\\s|^)${keyword.text}(\\s|$|<br>)`, "gi");
        // Заменяем ключевые слова на <span> с классом
        html = html.replace(regex, `$1<span class="${keyword.className}">${keyword.text}</span>$2`);
    });

    cell.innerHTML = html; // Обновляем содержимое ячейки
}

// Применяем функцию к каждой ячейке
statusCells.forEach(highlightKeywords);