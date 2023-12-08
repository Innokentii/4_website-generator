from flask import Flask, render_template, request, jsonify, Response
import sqlite3 as SQL
import os
import shutil

# Функция запуска сайта
app = Flask(__name__)
def create_app():
    return app

#===============================================================#
#                 Работа со страницами сайта                    #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Рендер тела сайта (запуск сайта);
@app.route('/')
@app.route('/designer')
def body():
    return render_template('designer.html')

#===============================================================#
#                    Глобальные переменные                      #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

#______наименования_____________________________________________
name_website = '123' # (имя сайта [нужно писать бех пробелов]);

#______глобальные пути__________________________________________


#===============================================================#
#                Работа_с_базой_данных_SQLite3                  #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

#===============================================================#
#                     Работа с запросами                        #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Запрос "POST" запись товаров "КОРЗИНА";
@app.route('/gen_website_1', methods=['POST'])
def basket_f():
    data = request.get_json(force=True)
    data = [data['data']]
    data = data[0]

    os.mkdir(f'website/{name_website}') # создание главной папки сайта;
    os.mkdir(f'website/{name_website}/database') # создание папки для хранения базы данных;
    os.mkdir(f'website/{name_website}/docs') # создание папки для хранения документации сайта;
    os.mkdir(f'website/{name_website}/orders') # создание папки для хранения запросов/заказов сайта;
    os.mkdir(f'website/{name_website}/static') # создание папки для хранения статических файлов для работы;
    os.mkdir(f'website/{name_website}/templates') # создание папки для хранения html файлов;
    os.mkdir(f'website/{name_website}/static/work_img') # создание папки для хранения рабочих изображений;

    # копирование рабочих файлов;
    shutil.copyfile('static/load_gif.gif', f'website/{name_website}/static/load_gif.gif')
    shutil.copyfile('static/windows_load.jpg', f'website/{name_website}/static/windows_load.jpg')
    shutil.copyfile('static/red_body.jpg', f'website/{name_website}/static/red_body.jpg')
    shutil.copyfile('static/red_windows_repl.jpg', f'website/{name_website}/static/red_windows_repl.jpg')
    shutil.copyfile('static/search.png', f'website/{name_website}/static/search.png')
    shutil.copyfile('static/burger_catalog.jpg', f'website/{name_website}/static/burger_catalog.jpg')
    shutil.copyfile('static/geolocation.png', f'website/{name_website}/static/geolocation.png')
    shutil.copyfile('static/1_main.txt', f'website/{name_website}/templates/1_main.html')
    shutil.copyfile('static/table.jpg', f'website/{name_website}/static/table.jpg')
    shutil.copyfile('static/gain_icon.png', f'website/{name_website}/static/gain_icon.png')
    shutil.copyfile('static/no_photo.jpg', f'website/{name_website}/static/no_photo.jpg')

    # страницы поиска товаров;
    if data[6][0]=='y':
        shutil.copyfile('static/2_search_css.css', f'website/{name_website}/static/2_search_css.css')
        shutil.copyfile('static/2_search_js.js', f'website/{name_website}/static/2_search_js.js')
        shutil.copyfile('static/2_search.html', f'website/{name_website}/templates/2_search.html')

    # страница корзина;
    if data[6][1]=='y':
        shutil.copyfile('static/3_basket_css.css', f'website/{name_website}/static/3_basket_css.css')
        shutil.copyfile('static/3_basket_js.js', f'website/{name_website}/static/3_basket_js.js')
        shutil.copyfile('static/3_basket.html', f'website/{name_website}/templates/3_basket.html')

    # стартовый файл "run.py";
    with open(f'website/{name_website}/run.py', 'w', encoding='utf-8') as filein:
        filein.write('from app import create_app\n\napp = create_app()\n\nif __name__ == "__main__":\n    app.run(debug=True)')

    # главный серверный файл сайта "app.py";
    with open(f'website/{name_website}/app.py', 'w', encoding='utf-8') as filein:
        filein.write('from flask import Flask, render_template, request, jsonify, Response\nimport sqlite3 as SQL\n')
        text = ''
        # импортируемые файлы;
        with open('static/app_py_1.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
        # глобальные переменные;
        with open('static/app_py_2.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
        # работа_с_базой_данных_SQLite3;
        with open('static/app_py_3.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
            # страницы поиска товаров;
            if data[6][0]=='y':
                with open('static/2_search_sql.txt', 'r', encoding='utf-8') as filein_work_child:
                    text = filein_work_child.read()
                    filein.write(text)
        # работа с запросами;
        with open('static/app_py_4.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
        # функции и классы;
        with open('static/app_py_5.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
        # работа со страницами;
        with open('static/app_py_6.txt', 'r', encoding='utf-8') as filein_work: 
            text = filein_work.read()
            filein.write(text)
            filein.write("\n# Рендер тела сайта (запуск сайта);\n@app.route('/')\n@app.route('/main')\ndef main_f():\n    render_template('main.html')\n    return render_template('1_main.html')")
            filein.write('\n# Рендер страницы "ГЛАВНАЯ";\n@app.route("/1_main")\ndef _1_main_f():\n    return render_template("1_main.html")\n')

            # страницы поиска товаров;
            if data[6][0]=='y':
                filein.write('\n# Рендер страницы "ПОИСК";\n@app.route("/2_search")\ndef _2_search_f():\n    return render_template("2_search.html")\n')

            # страница корзина;
            if data[6][1]=='y':
                filein.write('\n# Рендер страницы "ПОИСК";\n@app.route("/3_basket")\ndef _3_basket_f():\n    return render_template("3_basket.html")\n')

            # дополнительные каталоги;
            for str in data[5]:
                filein.write(f'\n# Рендер страницы "{str}";\n@app.route("/{str}")\ndef _{str}_f():\n    return render_template("{str}.html")\n')
        
    # главная страница "main.html";
    with open(f'website/{name_website}/templates/main.html', 'w', encoding='utf-8') as filein:
        text = ''
        with open(f'static/main.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(f'{text}')
        with open(f'static/WxH.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(f'{text}')
        # 1_иконка загрузки страницы;
        if data[0] == 2:
            filein.write('    <div class="load_icon_cl" id="load_icon_id">\n        <!--показ логотипа организации при загрузке-->\n    </div>')
        if data[0] == 3:
            filein.write('\n    <div class="load_modal_opa_cl" id="load_modal_opa_id">\n        <!--прозначное окно модального окна-->\n    </div>')
            filein.write('\n    <div class="load_modal_car_cl" id="load_modal_car_id">\n        <!--карточка модального окна-->\n        <div>Загрузка...</div>\n        <img src="static/load_gif.gif" alt="Н/Ф">\n    </div>\n')
        #3_тип шапки;
        if data[2] == 1:
            filein.write('\n    <div class="head_website_dempf_cl" id="head_website_dempf_id">\n        <!--Фиксированный (демпфер)-->\n    </div>\n     <div class="head_website_cl" id="head_website_id">\n        <!--Фиксированный-->\n')
        if data[2] == 2:
            filein.write('\n    <div class="head_website_stationary_cl" id="head_website_stationary_id">\n        <!--Стационарный-->\n')
        # 5_Наличие рабочих блоков;
        for num in range(6):
            if data[4][num] == 'y':
                with open(f'static/div_{num+1}_main.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
                filein.write(text)

        filein.write('    </div>\n')

        filein.write('\n    {% block main %}\n    {% endblock %}\n')

        with open('static/Body_html.txt', 'r', encoding='utf-8') as filein_work:
            text = filein_work.read()
            filein.write(text)
        
        #4_заметка;
        if data[3] == 2:
            filein.write('\n    <div class="note_cl" id="note_id">\n        <!--заметка-->\n        <div>Заметка</div>\n    </div>')

        filein.write('\n    <script src="/static/main_js.js"></script>\n</body>\n</html>')

    # главный "main_css.css";
    with open(f'website/{name_website}/static/main_css.css', 'w', encoding='utf-8') as filein:
        # _______ГЛОБАЛЬНЫЕ_ПЕРЕМЕННЫЕ_________
        filein.write('/*=================================================================================*/\n/*                             ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ                               */\n/*VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV*/\n')
        filein.write('\n:root {\n')

        # 1_иконка загрузки страницы;
        filein.write('    --w_h_modal_win: 200px; /*(ширина и высота карточки модального окна);*/\n    --bord_modal_win: 4px; /*(толщина рамки border карточки модального окна);*/\n')
        #3_тип шапки;
        filein.write('    --height__head_website: 80px; /*(высота шапки сайта);*/\n    --bord_head_website: 2px; /*(толщина рамки шапки сайта));*/\n')
        filein.write('}\n')

        # ___________СТИЛИЗАЦИЯ_____________
        filein.write('\n/*=================================================================================*/\n/*                                  СТИЛИЗАЦИЯ                                    */\n/*VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV*/\n')

        with open('static/BODY.txt', 'r', encoding='utf-8') as filein_work:
            text = filein_work.read()
            filein.write(text)
        with open('static/Body_css.txt', 'r', encoding='utf-8') as filein_work:
            text = filein_work.read()
            filein.write(text)

        # 2_backgraund body;
        filein.write('\nbody {\n')
        if data[1] == 1:
            filein.write('    background: white;\n')
        if data[1] == 2:
            filein.write('    background: linear-gradient(45grad, rgb(229, 192, 192), rgb(216, 119, 119), rgb(219, 44, 44), red);\n')
        if data[1] == 3:
            filein.write('    background-image: url(static/red_body.jpg);\n    background-size: cover;\n    background-position: 50% 50%;\n')
        if data[1] == 4:
            filein.write('    background-image: url(static/red_windows_repl.jpg);\n    background-size: 100px auto;\n')
        filein.write('}\n')
        
        # 1_иконка загрузки страницы;
        filein.write('\n/*________1_иконка загрузки страницы______________*/\n')
        if data[0] == 2:
            filein.write('\n.load_icon_cl {\n    /*показ логотипа организации при загрузке*/\n    width: 100%;\n    height: 100%;\n    position: fixed;\n    background-image: url(static/windows_load.jpg);\n    background-size: cover;\n    background-position: 50% 50%;\n    z-index: 997;\n}\n')
        if data[0] == 3:
            filein.write('\n.load_modal_opa_cl {\n    /*прозначное окно модального окна*/\n    width: 100%;\n    height: 100%;\n    position: fixed;\n    background-color: rgb(75, 73, 73);\n    opacity: 0.4;\n    z-index: 998;\n}\n')
            filein.write('\n.load_modal_car_cl {\n    /*карточка модального окна*/\n    position: fixed;\n    top: calc(50% - (var(--w_h_modal_win)/2) - var(--bord_modal_win));\n    left: calc(50% - (var(--w_h_modal_win)/2) - var(--bord_modal_win));\n    width: var(--w_h_modal_win);\n    height: var(--w_h_modal_win);\n    display: flex;\n    flex-direction: column;\n    border: solid var(--bord_modal_win) black;\n    background-color: rgb(60, 60, 193);\n    border-radius: 30px;\n    display: flex;\n    flex-direction: column;\n    align-items: center;\n    justify-content: center;\n    font-size: 35px;\n    font-weight: bolder;\n    gap: 5px;\n    z-index: 999;\n}\n')
            filein.write('\n.load_modal_car_cl > img {\n    /*гифка загрузки*/\n    width: 80px;\n    height: 80px;\n}\n')
        
        #3_тип шапки;
        filein.write('\n/*________3_тип шапки______________*/\n')
        if data[2] == 1:
            filein.write('\n.head_website_dempf_cl {\n    /*фикцированный (демпфер)*/\n    width: calc(100% - var(--bord_head_website)*2);\n    height: var(--height__head_website);\n}\n')
            filein.write('\n.head_website_cl {\n    /*фикцированный*/\n    width: 100%;\n    height: var(--height__head_website);\n    border-bottom: solid var(--bord_head_website) black;\n    position: fixed;\n    top: 0;\n    left: 0;\n    display: grid;\n    grid-template-columns: 0fr 0.7fr 0.7fr 0fr 0.5fr 0.4fr;\n    grid-template-rows: 1fr;\n    background-color: white;\n}\n')
            filein.write('\n@media (max-width: 768px) {\n    .head_website_cl, .head_website_dempf_cl {\n        display: flex;\n        flex-direction: row;\n        justify-content: space-around;\n        flex-wrap: wrap;\n        height: auto;\n        gap: 5px;\n    }\n}\n')
        if data[2] == 2:
            filein.write('\n.head_website_stationary_cl {\n    /*стационарный*/\n    width: 100%;\n    height: var(--height__head_website);\n    border-bottom: solid var(--bord_head_website) black;\n    display: grid;\n    grid-template-columns: 0fr 0.7fr 0.7fr 0fr 0.5fr 0.4fr;\n    grid-template-rows: 1fr;\n    background-color: white;\n}\n')
            filein.write('\n@media (max-width: 768px) {\n    .head_website_stationary_cl {\n        display: flex;\n        flex-direction: row;\n        justify-content: space-around;\n        flex-wrap: wrap;\n        height: auto;\n        gap: 5px;\n    }\n}\n')
        #4_заметка;
        if data[3] == 2:
            filein.write('\n.note_cl {\n    /*заметка*/\n    width: 100px;\n    height: 100px;\n    position: fixed;\n    bottom: 100px;\n    right: 50px;\n    background-color: rgb(121, 121, 206);\n    font-size: 20px;\n    font-weight: bolder;\n    display: flex;\n    align-items: center;\n    justify-content: center;\n    border: solid 4px black;\n}\n')
        # 5_Наличие рабочих блоков;
        for num in range(6):
            if data[4][num] == 'y':
                with open(f'static/css_{num+1}_main.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
                filein.write(text)

    # главный "main_js.js";
    with open(f'website/{name_website}/static/main_js.js', 'w', encoding='utf-8') as filein:
        text = ''
        # импортируемые файлы;
        with open('static/main_js_1.txt', 'w', encoding='utf-8') as filein_work: filein_work.write("'use strict' // Установка JS на строгий режим написания кода;\n\n//===================================================================================================//\n//                                  Импортированные файлы и модули                                   //\n//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//\n\n")
        with open('static/main_js_1.txt', 'a', encoding='utf-8') as filein_work: filein_work.write("")
        with open('static/main_js_1.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(text)

        # глобальные переменные;
        with open('static/main_js_2.txt', 'w', encoding='utf-8') as filein_work: filein_work.write("\n//===================================================================================================//\n//                                       Глобальные переменные                                       //\n//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//\n\n")
        with open('static/main_js_2.txt', 'a', encoding='utf-8') as filein_work:
            # 1_иконка загрузки страницы;
            if data[0] == 2:
                filein_work.write("let load_icon = document.getElementById('load_modal_opa_id'); // (логотип организации при загрузке);\n")
            elif data[0] == 3:
                filein_work.write("let load_modal_opa = document.getElementById('load_modal_opa_id').style.display = 'none'; // (туман модального окна);\nlet load_modal_car = document.getElementById('load_modal_car_id').style.display = 'none'; // (карта модального окна);\n")
            else: 
                filein_work.write('')
        with open('static/main_js_2.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(text)

        # одноразовые функции и события;
        with open('static/main_js_3.txt', 'w', encoding='utf-8') as filein_work: filein_work.write("\n//===================================================================================================//\n//                                 Одноразовые функции и события                                     //\n//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//\n\n")
        with open('static/main_js_3.txt', 'a', encoding='utf-8') as filein_work:
            # 1_иконка загрузки страницы;
            if data[0] == 2:
                filein_work.write("load_icon.style.display = 'none'; // (скрытие логотипа организации при загрузке);\n")
            elif data[0] == 3:
                filein_work.write("load_modal_opa.style.display = 'none'; // (скрытие тумана модального окна);\nload_modal_car.style.display = 'none'; // (скрытие карточки модального окна);\n")
            else:
                filein_work.write('')
        with open('static/main_js_3.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(text)

        # многоразовые функции и события вызовов функций;
        with open('static/main_js_4.txt', 'w', encoding='utf-8') as filein_work: filein_work.write("\n//===================================================================================================//\n//                      Многоразовые функции и события вызовов функций                               //\n//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//\n\n")
        with open('static/main_js_4.txt', 'a', encoding='utf-8') as filein_work: filein_work.write("")
        with open('static/main_js_4.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(text)

        # Функции вызываемые другими функциями;
        with open('static/main_js_5.txt', 'w', encoding='utf-8') as filein_work: filein_work.write("\n//===================================================================================================//\n//                             Функции вызываемые другими функциями                                  //\n//VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV//\n\n")
        with open('static/main_js_5.txt', 'a', encoding='utf-8') as filein_work: filein_work.write("")
        with open('static/main_js_5.txt', 'r', encoding='utf-8') as filein_work: text = filein_work.read()
        filein.write(text)

    # дополнительные каталоги;
    for str in data[5]:
        with open(f'website/{name_website}/templates/{str}.html', 'w', encoding='utf-8') as filein:
            text = '{% extends "main.html" %}\n\n{% block main %}\n\n<link rel="stylesheet" href="/static/' + str + '_css.css">\n\n<div></div>\n\n<script src="/static/' + str + '_js.js"></script>\n\n{% endblock %}'
            filein.write(text)
        shutil.copyfile('static/CSS_copy.txt', f'website/{name_website}/static/' + str + '_css.css')
        shutil.copyfile('static/JS_copy.txt', f'website/{name_website}/static/' + str + '_js.js')

    return data 

#===============================================================#
#                      Функции и классы                         #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

