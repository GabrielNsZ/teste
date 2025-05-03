from database import create_tables
import task_manager
import notes
import client_manager
import reminder


def menu():
    print("\n=== LIFE FLOW ===")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Concluir tarefa")
    print("4. Deletar tarefa")
    print("5. Adicionar nota")
    print("6. Ver notas")
    print("7. Adicionar cliente")
    print("8. Ver clientes")
    print("9. Adicionar lembrete")
    print("10. Ver lembretes")
    print("0. Sair")


def handle_add_task():
    t = input("Título: ").strip()
    d = input("Descrição: ").strip()
    due = input("Prazo (YYYY-MM-DD): ").strip()
    if task_manager.add_task(t, d, due):
        print("✅ Tarefa adicionada com sucesso.")
    else:
        print("❌ Falha ao adicionar tarefa.")


def handle_list_tasks():
    tasks = task_manager.list_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for t in tasks:
        status = "✔" if t["completed"] else "✖"
        print(
            f"ID: {t['id']} | {status} {t['title']} - {t['description']} (Prazo: {t['due_date']})")


def handle_complete_task():
    try:
        tid = int(input("ID da tarefa: "))
        if task_manager.complete_task(tid):
            print("✅ Tarefa concluída.")
        else:
            print("❌ Não foi possível concluir a tarefa.")
    except ValueError:
        print("❌ ID inválido.")


def handle_delete_task():
    try:
        tid = int(input("ID da tarefa: "))
        if task_manager.delete_task(tid):
            print("✅ Tarefa deletada.")
        else:
            print("❌ Não foi possível deletar a tarefa.")
    except ValueError:
        print("❌ ID inválido.")


def handle_add_note():
    content = input("Conteúdo da nota: ").strip()
    if notes.add_note(content):
        print("✅ Nota adicionada.")
    else:
        print("❌ Falha ao adicionar nota.")


def handle_list_notes():
    for n in notes.list_notes():
        print(f"ID: {n['id']} | {n['content']}")


def handle_add_client():
    name = input("Nome: ").strip()
    email = input("Email: ").strip()
    if client_manager.add_client(name, email):
        print("✅ Cliente adicionado.")
    else:
        print("❌ Falha ao adicionar cliente.")


def handle_list_clients():
    for c in client_manager.list_clients():
        print(f"ID: {c['id']} | {c['name']} - {c['email']}")


def handle_add_reminder():
    msg = input("Mensagem: ").strip()
    date = input("Data e hora (YYYY-MM-DD HH:MM): ").strip()
    if reminder.add_reminder(msg, date):
        print("✅ Lembrete adicionado.")
    else:
        print("❌ Falha ao adicionar lembrete.")


def handle_list_reminders():
    for r in reminder.list_reminders():
        print(f"ID: {r['id']} | {r['message']} em {r['remind_at']}")


def main():
    create_tables()
    handlers = {
        "1": handle_add_task,
        "2": handle_list_tasks,
        "3": handle_complete_task,
        "4": handle_delete_task,
        "5": handle_add_note,
        "6": handle_list_notes,
        "7": handle_add_client,
        "8": handle_list_clients,
        "9": handle_add_reminder,
        "10": handle_list_reminders,
    }

    while True:
        menu()
        choice = input("Escolha uma opção: ").strip()
        if choice == "0":
            print("👋 Saindo...")
            break
        elif choice in handlers:
            handlers[choice]()
        else:
            print("❌ Opção inválida.")


if __name__ == "__main__":
    main()
