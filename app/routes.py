from flask import render_template, redirect, url_for, request
from app import app

# Список для хранения профилей пользователей
profiles = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        # Проверка, что все поля заполнены и возраст больше 0
        if name and city and hobby and age:
            try:
                age = int(age)
                if age > 0:
                    profiles.append({'name': name, 'city': city, 'hobby': hobby, 'age': age})
                    return redirect(url_for('index'))
            except ValueError:
                # Возраст должен быть целым числом
                pass

    # Отображаем форму и список профилей
    return render_template('index.html', profiles=profiles)
