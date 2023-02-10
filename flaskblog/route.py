from flask import render_template,flash,redirect,url_for,request
from flaskblog.form import Registration,Login,AssignmentPost,ReportCard
from flask_sqlalchemy import SQLAlchemy
from flaskblog import app,db,bcrypt
from flaskblog.model import User,Post,Student
from flask_login import login_user,current_user,UserMixin,logout_user,login_required
import secrets
from wtforms.validators import ValidationError


@app.route("/home")
def home():
    if current_user.is_authenticated:
        return render_template('index.html')
    else:
        return redirect(url_for('login'))
@app.route("/about")
def about():
   return render_template('about.html',title=title)
@app.route("/register",methods=['GET','POST'])
def register():
    form = Registration()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(name=form.name.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your Account have been created!','success')
        return redirect(url_for('login'))
    return render_template('signin.html',title='Register Page',form=form)
@app.route("/" ,methods=['GET','POST'])
def login():       
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            flash(f'Login Successful :  {user.name}!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful Please log in again or Register  !','danger')
    return render_template('my_login.html',title='Login Page',form=form)
@app.route("/timetable")
def timetable():
        if current_user.is_authenticated:
             return render_template('timetable.html',title='Time Table Page')
        else:
             return redirect(url_for('login'))
@app.route("/reportcard")
@login_required
def reportcard():
 if current_user.is_authenticated:
             studs = Student.query.all()
             return render_template('reportcard.html',title='Report Card Page',studs=studs)
@app.route("/admission")
def admission():
        if current_user.is_authenticated:
             return render_template('admission.html',title='Report Card Page')
        else:
             return redirect(url_for('login'))
@app.route("/geo")
def geo():
        if current_user.is_authenticated:
             return render_template('geo.html',title='Report Card Page')
        else:
             return redirect(url_for('login'))
@app.route("/java")
def java():
        if current_user.is_authenticated:
             return render_template('java.html',title='Report Card Page')
        else:
             return redirect(url_for('login'))
@app.route("/python")
def python():
        if current_user.is_authenticated:
             return render_template('python.html',title='Report Card Page')
        else:
             return redirect(url_for('login'))
@app.route("/lecturenote")
def lecturenote():
        if current_user.is_authenticated:
             posts = Post.query.all()
             return render_template('lecturenote.html',title='Report Card Page',posts=posts)

@app.route("/signout")
def signout():
        logout_user()
        return redirect(url_for('login'))
@app.route("/message",methods=['GET','POST'])
def message():
    return render_template('message.html',title='message')
@app.route("/new_ass",methods=['GET','POST'])
@login_required
def new_ass():
    form = AssignmentPost()
    if form.validate_on_submit():
        post =Post(course_title=form.CourseTitle.data,course_id=form.CourseNo.data,content=form.Content.data,deadline=form.Deadline.data,remark=form.Remark.data,max_score=form.MaximiumScore.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Your Assignment : {post.course_title} have been created!','success')
        return redirect(url_for('lecturenote'))
    return render_template('create_ass.html',title='Register Page',form=form,legend='New Assign')
@app.route("/add_stu",methods=["GET","POST"])
@login_required
def addstu():
        form=ReportCard()
        if form.validate_on_submit():
                check_student = Student.query.filter_by(student_id =form.ID.data).first()
                if check_student:
                   flash(f'The Student is already exist','danger')
                   return redirect(url_for('addstu'))
                student = Student(student_id=form.ID.data,student_name=form.Name.data,student_score=form.Score.data,student_grade=form.Grade.data,author=current_user)
                db.session.add(student)
                db.session.commit()
                flash(f'Record have been added!','success')
                return redirect(url_for('reportcard'))
        return render_template('create_stulist.html',title='Report Card Page',form=form)
@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('u_lecture.html',post=post)
@app.route("/post/<int:post_id>/update",methods=["GET","POST"])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    form=AssignmentPost()
    if post.author !=current_user:
        post(403)
    if form.validate_on_submit():
        post.course_title=form. CourseTitle.data
        post.course_id=form.CourseNo.data
        post.deadline=form.Deadline.data
        post.max_score=form.MaximiumScore.data
        post.content=form.Content.data
        db.session.commit()
        flash('Your Post has been updated','success')
        return redirect(url_for('lecturenote'))
    elif request.method =='GET':
     form.CourseTitle.data=post.course_title
     form.CourseNo.data=post.course_id
     form.Deadline.data=post.deadline
     form.MaximiumScore.data=post.max_score
     form.Content.data=post.content
    return render_template('create_ass.html',form=form,legend='Update Post')
with app.app_context():
    db.create_all()