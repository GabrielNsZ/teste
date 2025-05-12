import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


def connect():
    return sqlite3.connect('database.db')


def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        title TEXT,
                        description TEXT,
                        date TEXT,
                        importance TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS notes (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        title TEXT,
                        content TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()


def get_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    conn.close()
    if user and check_password_hash(user[2], password):
        return {"id": user[0], "username": user[1]}
    return None


def create_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    hashed_pw = generate_password_hash(password)
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
    conn.commit()
    conn.close()


def get_tasks(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE user_id=?", (user_id,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def add_task(user_id, title, description, date, importance):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_id, title, description, date, importance) VALUES (?, ?, ?, ?, ?)",
                   (user_id, title, description, date, importance))
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()
    conn.close()


def update_task(task_id, title, description, date, importance):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET title=?, description=?, date=?, importance=? WHERE id=?",
                   (title, description, date, importance, task_id))
    conn.commit()
    conn.close()


# FUNÇÕES DE NOTAS

def get_all_notes(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, content FROM notes WHERE user_id=?", (user_id,))
    notes = cursor.fetchall()
    conn.close()
    return notes


def add_note(user_id, title, content):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notes (user_id, title, content) VALUES (?, ?, ?)", (user_id, title, content))
    conn.commit()
    conn.close()


def delete_note(note_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE id=?", (note_id,))
    conn.commit()
    conn.close()


def update_note(note_id, title, content):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE notes SET title=?, content=? WHERE id=?",
                   (title, content, note_id))
    conn.commit()
    conn.close()
