from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Функция для проверки возраста
def is_valid_age(birthdate):
    today = datetime.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age >= 18

@app.route('/')
def index():
    return render_template('index.html', title="Главная")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        birthdate = request.form['birthdate']
        hobbies = request.form['hobbies']
        file = request.files['avatar']

        if not all([name, surname, birthdate, hobbies, file]):
            flash('Все поля обязательны для заполнения')
            return redirect(url_for('register'))

        if len(name) < 3:
            flash('Имя должно содержать не менее 3 символов!(если мегьше то увы)')
            return redirect(url_for('register'))

        try:
            birthdate = datetime.strptime(birthdate, '%Y-%m-%d')
            if not is_valid_age(birthdate):
                flash('Возраст должен быть больше 18 лет')
                return redirect(url_for('register'))
        except ValueError:
            flash('Некорректная дата рождения')
            return redirect(url_for('register'))

        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return render_template('account.html', name=name, surname=surname, birthdate=birthdate.strftime('%Y-%m-%d'), hobbies=hobbies, avatar=filename)

    return render_template('register.html', current_year=datetime.now().year)

if __name__ == '__main__':
    app.run(debug=True)
