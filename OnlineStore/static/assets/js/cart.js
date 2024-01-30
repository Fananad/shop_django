$('.minus').click(function () { // вызов функции при клике на элемент
    var $input = $(this).parent().find('input'); // объявление переменной и присвоение ей значения поля ввода
    var count = parseInt($input.val()) - 1; // объявление переменной, преобразование значения в число и уменьшение его на 1
    count = count < 1 ? 1 : count; // условие, которое говорит "Если значение переменной меньше 1 то запиываем 1"
    $input.val(count); // присвоение атрибута value переменной count переменной $input
  });
  $('.plus').click(function () { // вызов функции при клике на элемент
    var $input = $(this).parent().find('input'); // объявление переменной и присвоение ей значения поля ввода
    $input.val(parseInt($input.val()) + 1); // объявление переменной, преобразование значения в число и увеличение его на 1
  });