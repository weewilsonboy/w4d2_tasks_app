from flask import Flask, render_template, redirect, Blueprint, request
from app import db
from models import Task, User
tasks_blueprint=Blueprint("tasks",__name__)

@tasks_blueprint.route('/tasks')
def tasks():
    tasks = Task.query.all()
    return render_template("tasks/index.jinja", tasks=tasks)

@tasks_blueprint.route('/tasks', methods=['POST'])
def create():
    description = request.form['description']
    duration = request.form['duration']
    completed = 'completed' in request.form
    user_id = request.form['user_id']

    task = Task(description=description, duration=duration, completed=completed, user_id=user_id)
    db.session.add(task)
    db.session.commit()
    return redirect('/tasks')


@tasks_blueprint.route('/tasks/<id>')
def individual(id):
    wanted_task = Task.query.get(id)
    return render_template("/tasks/individual.jinja", task=wanted_task)

@tasks_blueprint.route('/tasks/new')
def new():
    users = User.query.all()
    return render_template("/tasks/new.jinja", users=users)
@tasks_blueprint.route('/tasks/<id>/edit')
def edit_page(id):
    users = User.query.all()
    task = Task.query.get(id)
    return render_template('tasks/edit.jinja', task=task, users=users)
@tasks_blueprint.route('/tasks/<id>', methods=['POST'])
def update(id):
    description = request.form['description']
    duration = request.form['duration']
    completed = 'completed' in request.form
    user_id = request.form['user_id']

    task = Task.query.get(id)
    task.description = description
    task.user_id = user_id
    task.duration = duration
    task.completed = completed
    db.session.commit()

    return redirect('/tasks')

@tasks_blueprint.route('/tasks/<id>/delete', methods=['POST'])
def delete(id):

    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/tasks')

@tasks_blueprint.route('')
def home():
    return redirect('/tasks')
