# from flask import Flask, render_template, url_for, \
#     flash, request, session, redirect, abort
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '5443d109810cff4cf27c1b69b0ede52abd1db3a86dbed1'
# menu = [
#     {"name": "Главная", "url": "home"},
#     {"name": "О создателях страницы", "url": "about_creators"},
#     {"name": "Связь", "url": "bonds"}
# ]
#
#
# @app.route("/home")
# @app.route("/")
# def home():
#     print(url_for('home'))
#     return render_template("home.html", title="Главная страница", menu=menu)
#
#
# @app.route("/about_creators")
# def about_creators():
#     print(url_for("about_creators"))
#     return render_template("about_creators.html", title="О странице", menu=menu)
#
#
# @app.route("/bonds", methods=["POST", "GET"])
# def bonds():
#     # print(url_for("bonds.html"))
#     if request.method == 'POST':
#         print(request.form)
#         if len(request.form['username']) > 2:
#             flash("Сообщение Отправлено Успешно", category='success')
#         else:
#             flash("Ошибка Отправки Данных", category='error')
#
#     return render_template("bonds.html", title="Связь", menu=menu)
#
#
# @app.route("/profile/<username>")
# def profile(username):
#     if 'userLogged' not in session or session['userLogged'] != username:
#         abort(401)
#         return f"Пользователь: {username}"
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page404.html', title="Страница Не Найдена", menu=menu)
#
#
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     if 'userLogged' == session:
#         return redirect(url_for('profile', username=session['userLogged']))
#     elif request.method == 'POST' and request.form['username'] == 'Aleksey' \
#             and request.form['passw'] == '654321':
#         session['userLogged'] = request.form['username']
#         return redirect(url_for('profile', username=session['userLogged']))
#     return render_template('login.html', title="Авторизация", menu=menu)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)