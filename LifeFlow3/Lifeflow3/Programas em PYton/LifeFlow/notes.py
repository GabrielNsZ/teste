from database import get_connection
from sqlite3 import Error
from typing import List, Tuple


def add_note(content: str) -> bool:
    try:
        with get_connection() as conn:
            conn.execute("INSERT INTO notes (content) VALUES (?)", (content,))
        return True
    except Error as e:
        print(f"[Erro ao adicionar nota] {e}")
        return False


def list_notes() -> List[Tuple]:
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM notes").fetchall()
    except Error as e:
        print(f"[Erro ao listar notas] {e}")
        return []
