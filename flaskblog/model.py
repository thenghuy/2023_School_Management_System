from flaskblog import db,app,login_manager
import datetime
from flask_login import UserMixin
@login_manager.user_loader
def load_user (user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    #Create Column
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20),unique=True,nullable=False)
    email = db.Column(db.String(120),unique=True,nullable=False)
    image_file = db.Column(db.String(20),nullable=False,default='default.jpg')
    password=db.Column(db.String(60),nullable=False)
    posts = db.relationship('Post',backref='author',lazy=True)
    students = db.relationship('Student',backref='author',lazy=True)
    def __repr__(self) :
        return f"User('{self.id}','{self.name}','{self.email}','{self.image_file}')"
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    course_id=db.Column(db.String(100),nullable=False)
    course_title = db.Column(db.String(100),nullable=False)
    date_posted =db.Column(db.DateTime,nullable=False,default=datetime.datetime.utcnow())
    deadline = db.Column(db.DateTime,nullable=False)
    content = db.Column(db.Text,nullable=False)
    max_score = db.Column(db.Integer,nullable=False)
    remark = db.Column(db.Text,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f"Post('{self.author.name}':'{self.course_title}','{self.content}','{self.date_posted})"

class Student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    student_id = db.Column(db.Integer,nullable=False,unique=True)
    student_name = db.Column(db.String(100),nullable=False)
    student_score=db.Column(db.Integer,nullable=False)
    student_grade=db.Column(db.String(10),nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    def __repr__(self):
        return f"Post('{self.student_name}','{self.student_id}')"