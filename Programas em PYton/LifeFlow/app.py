# app.py
from flask import Flask, render_template, request, redirect
import task_manager
import notes
import client_manager
import reminder
from database import create_tables

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/tasks", methods=["GET", "POST"])
def tasks():
    if request.method == "POST":
        task_manager.add_task(
            request.form["title"],
            request.form["description"],
            request.form["due_date"]
        )
        return redirect("/tasks")
    tasks = task_manager.list_tasks()
    return render_template("tasks.html", tasks=tasks)


@app.route("/complete_task/<int:task_id>")
def complete_task(task_id):
    task_manager.complete_task(task_id)
    return redirect("/tasks")


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    task_manager.delete_task(task_id)
    return redirect("/tasks")


@app.route("/notes", methods=["GET", "POST"])
def notes_page():
    if request.method == "POST":
        notes.add_note(request.form["content"])
        return redirect("/notes")
    return render_template("notes.html", notes=notes.list_notes())


@app.route("/clients", methods=["GET", "POST"])
def clients():
    if request.method == "POST":
        client_manager.add_client(
            request.form["name"],
            request.form["email"]
        )
        return redirect("/clients")
    return render_template("clients.html", clients=client_manager.list_clients())


@app.route("/reminders", methods=["GET", "POST"])
def reminders():
    if request.method == "POST":
        reminder.add_reminder(
            request.form["message"],
            request.form["remind_at"]
        )
        return redirect("/reminders")
    return render_template("reminders.html", reminders=reminder.list_reminders())


if __name__ == '__main__':
    app.run(debug=True, port=8080)
