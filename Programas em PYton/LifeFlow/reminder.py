from database import get_connection
from sqlite3 import Error
from typing import List, Tuple


def add_reminder(message: str, remind_at: str) -> bool:
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO reminders (message, remind_at) VALUES (?, ?)",
                (message, remind_at)
            )
        return True
    except Error as e:
        print(f"[Erro ao adicionar lembrete] {e}")
        return False


def list_reminders() -> List[Tuple]:
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM reminders").fetchall()
    except Error as e:
        print(f"[Erro ao listar lembretes] {e}")
        return []
