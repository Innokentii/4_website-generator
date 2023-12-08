from flask import Flask, render_template, request, jsonify, Response
import sqlite3 as SQL
from flask import Flask, render_template, request, jsonify, Response
import sqlite3 as SQL

# Функция запуска сайта
app = Flask(__name__)
def create_app():
    return app


#===============================================================#
#                    Глобальные переменные                      #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#


#===============================================================#
#                Работа_с_базой_данных_SQLite3                  #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#


PATH_work = '' # (путь до базы данных);

# База данных для списка товаров;
connect = SQL.connect(f'{PATH_work}database/SQLite3_products.db')
cursor = connect.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                path_image text,
                path_gain_image text,
                product_name text,
                main_characteristic text,
                article_number text,
                catalog_number text,
                country text,
                release_date text,
                cost int,
                quantity int,
                measurement text
                description text,
                big_description text
                );""")
connect.commit()
connect.close

#===============================================================#
#                     Работа с запросами                        #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#

# Запрос "POST";
@app.route('/post_request_1', methods=['POST'])
def post_request_1_f():
    post_request = request.get_json(force=True)
    post_request = [post_request['name_basket']]
    if request.method == 'GET':
        return None
    return post_request

# Запрос "GET";
@app.route('/get_request_1', methods=['GET'])
def get_request_1_f():
    data = 1
    if request.method == 'POST':
        return None
    return jsonify(data)


#===============================================================#
#                      Функции и классы                         #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#


#===============================================================#
#                    Работа со страницами                       #
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV#


# Рендер тела сайта (запуск сайта);
@app.route('/')
@app.route('/main')
def main_f():
    render_template('main.html')
    return render_template('1_main.html')
# Рендер страницы "ГЛАВНАЯ";
@app.route("/1_main")
def _1_main_f():
    return render_template("1_main.html")

# Рендер страницы "ПОИСК";
@app.route("/2_search")
def _2_search_f():
    return render_template("2_search.html")

# Рендер страницы "ПОИСК";
@app.route("/3_basket")
def _3_basket_f():
    return render_template("3_basket.html")

# Рендер страницы "block_1";
@app.route("/block_1")
def _block_1_f():
    return render_template("block_1.html")

# Рендер страницы "block_2";
@app.route("/block_2")
def _block_2_f():
    return render_template("block_2.html")

# Рендер страницы "block_3";
@app.route("/block_3")
def _block_3_f():
    return render_template("block_3.html")

# Рендер страницы "block_4";
@app.route("/block_4")
def _block_4_f():
    return render_template("block_4.html")

# Рендер страницы "block_5";
@app.route("/block_5")
def _block_5_f():
    return render_template("block_5.html")
