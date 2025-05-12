# app.py
from flask import Flask, render_template, request, redirect, session, url_for
from models import init_db, get_user, create_user, get_tasks, add_task, delete_task, update_task
from models import get_all_notes, add_note, delete_note, update_note
from datetime import datetime
import os
from models import init_db

app = Flask(__name__)
app.secret_key = 'secreta'

# Verifica se o banco já existe, senão cria
if not os.path.exists('database.db'):
    init_db()


@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = get_user(request.form['username'], request.form['password'])
        if user:
            session['user_id'] = user['id']
            return redirect(url_for('dashboard'))
        return render_template('login.html', error='Credenciais inválidas')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        create_user(request.form['username'], request.form['password'])
        return redirect(url_for('login'))
    return render_template('register.html')


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')


@app.route('/tasks')
def tasks():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    tarefas = get_tasks(user_id)
    return render_template('tasks.html', tasks=tarefas)


@app.route('/add_task', methods=['POST'])
def add_task_route():
    user_id = session['user_id']
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']
    importance = request.form['importance']
    add_task(user_id, title, description, date, importance)
    return redirect(url_for('tasks'))


@app.route('/delete_task/<int:task_id>')
def delete_task_route(task_id):
    delete_task(task_id)
    return redirect(url_for('tasks'))


@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task_route(task_id):
    title = request.form['title']
    description = request.form['description']
    date = request.form['date']
    importance = request.form['importance']
    update_task(task_id, title, description, date, importance)
    return redirect(url_for('tasks'))


@app.route('/notes', methods=['GET', 'POST'])
def notes():
    if 'user_id' not in session:  # Adicione esta verificação
        return redirect(url_for('login'))

    user_id = session['user_id']

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        add_note(user_id, title, content)
        return redirect(url_for('notes'))

    all_notes = get_all_notes(user_id)
    return render_template('notes.html', notes=all_notes)


@app.route('/delete_note/<int:note_id>')
def delete_note_route(note_id):
    delete_note(note_id)
    return redirect(url_for('notes'))


@app.route('/update_note/<int:note_id>', methods=['POST'])
def update_note_route(note_id):
    title = request.form['title']
    content = request.form['content']
    update_note(note_id, title, content)
    return redirect(url_for('notes'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
