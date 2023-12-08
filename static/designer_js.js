'use strict' // Установка JS на строгий режим написания кода;
//===================================================================================================//
//                                  Импортированные файлы и модули                                   //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

//===================================================================================================//
//                                       Глобальные переменные                                       //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

let num_main_1 = 0; //(иконка загрузки страницы);
let num_main_2 = 0; //(backgraund body);
let num_head_1 = 0; //(тип шапки);
let num_head_2 = 0; //(стиль шапки);
let num_head_3 = []; //(наличие рабочих блоков);
let radio_head_text = 0; //(количество каталогов);
let num_head_4 = 0; //(Конструкция шапки);
let radio_head_text_block = document.getElementById('radio_head_text_id'); // (-количество каталогов);
let dividing_catalogs = document.getElementById('dividing_catalogs_id'); // (количество и наименование доп. каталогов);
let num_count = 0; // (количество дополнительных каталогов);
let array_catalog = []; // (наименования дополнительных каталогов);
let fun_page_footer = []; //(функциональные страницы);

//===================================================================================================//
//                                 Одноразовые функции и события                                     //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//



//===================================================================================================//
//                      Многоразовые функции и события вызовов функций                               //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

function fun_start_f() {
    //_________________Главный каркас сайта_________________//
    //(иконка загрузки страницы);
    num_main_1 = cycle_for_f('radio_main_1_');
    //(backgraund body);
    num_main_2 = cycle_for_f('radio_main_2_');
    //_________________шапка сайта_________________//
    //(тип шапки);
    num_head_1 = cycle_for_f('radio_head_1_');
    //(стиль шапки);
    num_head_2 = cycle_for_f('radio_head_2_');
    //(Наличие рабочих блоков);
    for (let i=1; i<100; i++) {
        if (document.getElementById(`radio_head_3_${i}_id`)) {
            if (document.getElementById(`radio_head_3_${i}_id`).checked == true) {
                num_head_3.push('y');
            }
            else {
                num_head_3.push('n');
            }
        }
    }

    // (дополнительные каталоги);
    for (let n=0; n<num_count; n++) {
        let name_catalog = document.getElementById(`new_input_${n+1}_id`).value;
        array_catalog.push(name_catalog);
    }

    //(функциональные страницы);
    for (let i=1; i<100; i++) {
        if (document.getElementById(`radio_footer_1_${i}_id`)) {
            if (document.getElementById(`radio_footer_1_${i}_id`).checked == true) {
                fun_page_footer.push('y');
            }
            else {
                fun_page_footer.push('n');
            }
        }
    }

    // Генерация сайта №1
    gen_website_f('/gen_website_1', [num_main_1, num_main_2, num_head_1, num_head_2, num_head_3, array_catalog, fun_page_footer]);
}

radio_head_text_block.addEventListener('input', _=>{
    console.log(1);
    setTimeout(_=>{
        num_count = Number(radio_head_text_block.value);
        if (num_count < 0) {
            num_count = 0;
            radio_head_text_block.value = 0;
        }

        if (num_count > 100) {
            num_count = 100;
            radio_head_text_block.value = 100;
        }

        for (let n=0; n<100; n++) {
            let el_span = document.getElementById(`new_span_${n+1}_id`);
            try {el_span.parentNode.removeChild(el_span);}
            catch {console.log('такого элемента нет')};
            let el_input = document.getElementById(`new_input_${n+1}_id`);
            try {el_input.parentNode.removeChild(el_input);}
            catch {console.log('такого элемента нет')};
        }

        for (let n=0; n<num_count; n++) {
            let new_span = document.createElement('span');
            new_span.innerText = `наи. каталога №${n+1}: `;
            new_span.id = `new_span_${n+1}_id`;
            let new_input = document.createElement('input');
            new_input.type = 'text';
            new_input.id = `new_input_${n+1}_id`;
            new_input.value = `block_${n+1}`;
            new_span.append(new_input);
            dividing_catalogs.append(new_span);
        }

    }, 100);
});

//===================================================================================================//
//                             Функции вызываемые другими функциями                                  //
//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//

// POST запросы;
function gen_website_f(name_data, data) {
    let xhr = new XMLHttpRequest();
    xhr.open('POST', `${name_data}`, true); 
    xhr.setRequestHeader('Content-type', "application/x-www-form-urlencoded");
    xhr.send(JSON.stringify({ "data": data }));
}

// Генерации запросов;
function cycle_for_f(data) {
    for (let i=1; i<100; i++) {
        try {
            if (document.getElementById(`${data}${i}_id`).checked == true) {
                return(i)
            }
        }
        catch {
            console.log('нету выбора')
        }
    }
};
