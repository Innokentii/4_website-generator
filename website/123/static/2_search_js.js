'use strict' // Установка JS на строгий режим написания кода;

//===================================================================================================//
//                                  Импортированные файлы и модули                                   //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//


//===================================================================================================//
//                                       Глобальные переменные                                       //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

let table_icon_img = document.getElementById('table_icon_img_id'); // (кнопка для вывода данных в таблицу);
let table_gain_icon_img = document.getElementById('table_gain_icon_img_id'); // (кнопка для вывода данных в крупном блоке);
let serch_table_parents = document.getElementById('serch_table_parents_id'); // (данные о товарах в табличку);
let large_block_parents = document.getElementById('large_block_parents_id'); // (данные о товарах в крупном блоке);
let big_description_fog = document.getElementById('big_description_fog_id'); // (туман модального окна товаров);
let big_description = document.getElementById('big_description_id'); // (карточка подробного описания товаров);

//===================================================================================================//
//                                 Одноразовые функции и события                                     //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

large_block_parents.style.display = 'none'; // (скрытие данных о товарах в крупном блоке);
big_description_fog.style.display = 'none'; // (скрытие тумана модального окна товаров);
big_description.style.display = 'none'; // (скрытие карточки подробного описания товаров);

//===================================================================================================//
//                      Многоразовые функции и события вызовов функций                               //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

table_icon_img.addEventListener('click', _=>{
    // функция перевода данных товаров в табличный вид;
    serch_table_parents.style.display = 'flex'; // (показ данных о товарах в табличку);
    large_block_parents.style.display = 'none'; // (скрытие данных о товарах в крупном блоке);
});

table_gain_icon_img.addEventListener('click', _=>{
    // функция перевода данных товаров в вид крупных блоков;
    serch_table_parents.style.display = 'none'; // (скрытие данных о товарах в табличку);
    large_block_parents.style.display = 'flex'; // (показ данных о товарах в крупном блоке);
});

//===================================================================================================//
//                             Функции вызываемые другими функциями                                  //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//


