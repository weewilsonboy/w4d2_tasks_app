from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
#for new project, change tasks_app to new DB name
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://wilson:password@localhost:5432/tasks_app"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from controllers.tasks_controller import tasks_blueprint

app.register_blueprint(tasks_blueprint)





# class User(db.Model):
#     __tablename__ = "users"

#     id = db.Column(db.Integer, primary_key = True) #primary_key will auto increment id
#     first_name = db.Column(db.String(64))
#     last_name = db.Column(db.String(64))
#     tasks =db.relationship("Task", backref='user', lazy=True) 
#     #backref creates on the task a user property, so you can do task.user
#     # lazy is a setting to only load what is needed for a relation, so for true it will only load what is absolutely necessary

#     def __repr__(self):
#         return f"<User {self.id}: {self.first_name} {self.last_name}>"

# class Task(db.Model):
#     __tablename__ ="tasks"

#     id = db.Column(db.Integer, primary_key = True) #primary_key will auto increment id
#     description = db.Column(db.Text())
#     duration = db.Column(db.Integer)
#     completed = db.Column(db.Boolean, default=False)
#     user_id = db.Column(db.Integer, db.ForeignKey("users.id")) #table_name.primary_key_column

#     def __repr__(self):
#         return f"<Task {self.id}: {self.description}>"

# @app.route('/')
# def hello_world():
#     #Delete all rows
#     Task.query.delete() #immediate delete
#     User.query.delete()

#     sky = User(first_name = "Sky", last_name = "Su")
#     jason = User(first_name = "Jason", last_name = "Sweeney")

#     db.session.add(sky) # stage changes
#     print("sky before commit")
#     print(sky)

#     db.session.add(jason) # stage changes
#     db.session.commit() # commit changes
#     print("sky after commit")
#     print(sky)

#     # get all the users
#     users = User.query.all()

#     print("Get all the users")
#     print(users)

#     # get a user by ID
#     found_user = User.query.get(jason.id)
#     print(f"Get user by id = {jason.id}")
#     print(found_user)

#     # create tasks

#     task1 = Task(description="Survive this lesson", duration=120, user=sky)
#     db.session.add(task1)
#     task2 = Task(description="Survive the next lesson", duration=60, completed=True, user=jason)
#     db.session.add(task2)
#     db.session.commit()

#     #get all the tasks

#     all_tasks = Task.query.all()
#     print("Get all the tasks")
#     print(all_tasks)

#     #print out jasons tasks

#     print("Jason's tasks")
#     print(jason.tasks)

#     print("task[0]'s user")
#     print(all_tasks[0].user.first_name)

#     # mark task1 as completed
#     task1.completed=True
#     db.session.commit()

#     #delete
#     db.session.delete(task2)
#     db.session.commit()
    
    
#     return "Hello, World"