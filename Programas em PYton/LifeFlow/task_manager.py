from database import get_connection
from sqlite3 import Error
from typing import List, Tuple, Optional


def add_task(title: str, description: str, due_date: str) -> bool:
    try:
        with get_connection() as conn:
            conn.execute(
                "INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)",
                (title, description, due_date)
            )
        return True
    except Error as e:
        print(f"[Erro ao adicionar tarefa] {e}")
        return False


def list_tasks() -> List[Tuple]:
    try:
        with get_connection() as conn:
            return conn.execute("SELECT * FROM tasks").fetchall()
    except Error as e:
        print(f"[Erro ao listar tarefas] {e}")
        return []


def complete_task(task_id: int) -> bool:
    try:
        with get_connection() as conn:
            conn.execute(
                "UPDATE tasks SET completed = 1, completed_at = CURRENT_TIMESTAMP WHERE id = ?",
                (task_id,)
            )
        return True
    except Error as e:
        print(f"[Erro ao concluir tarefa] {e}")
        return False


def delete_task(task_id: int) -> bool:
    try:
        with get_connection() as conn:
            conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        return True
    except Error as e:
        print(f"[Erro ao deletar tarefa] {e}")
        return False
