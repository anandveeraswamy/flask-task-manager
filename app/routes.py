from app import app
from flask import render_template, request, redirect, url_for

tasks = []

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")


@app.route("/tasks")
def task_list():
    return render_template("tasks.html", tasks=tasks)


@app.route("/add_task", methods=["GET"])
def add_task_get():
    return render_template("add_task.html")


@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form.get("task")
    tasks.append(task)
    return redirect(url_for("task_list"))


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):
    if 0 <= task_id <= len(tasks):
        tasks.pop(task_id)
    return redirect(url_for("task_list"))
