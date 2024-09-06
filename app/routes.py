from flask import render_template, redirect, url_for, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']
        # После успешного ввода данных перенаправляем пользователя на страницу результата
        return redirect(url_for('result', name=name, city=city, hobby=hobby, age=age))
    return render_template('index.html')

@app.route('/result')
def result():
    name = request.args.get('name')
    city = request.args.get('city')
    hobby = request.args.get('hobby')
    age = request.args.get('age')
    return render_template('result.html', name=name, city=city, hobby=hobby, age=age)
