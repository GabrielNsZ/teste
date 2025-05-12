from database import get_connection
from sqlite3 import Error
from typing import List, Tuple


def add_client(name: str, email: str) -> bool:
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO clients (name, email) VALUES (?, ?)",
                (name, email)
            )
        return True
    except Error as e:
        print(f"[Erro ao adicionar cliente] {e}")
        return False


def list_clients() -> List[Tuple]:
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM clients").fetchall()
    except Error as e:
        print(f"[Erro ao listar clientes] {e}")
        return []
