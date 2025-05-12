import sqlite3
from sqlite3 import Connection


def get_connection() -> Connection:
    conn = sqlite3.connect("lifeflow.db")
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn


def create_tables() -> None:
    with get_connection() as conn:
        c = conn.cursor()

        # Tarefas
        c.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                completed INTEGER DEFAULT 0,
                completed_at TEXT
            )
        """)

        # Notas
        c.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL
            )
        """)

        # Clientes
        c.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        # Lembretes
        c.execute("""
            CREATE TABLE IF NOT EXISTS reminders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT NOT NULL,
                remind_at TEXT NOT NULL
            )
        """)

        conn.commit()
