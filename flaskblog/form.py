from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,IntegerField,DateField,FileField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flaskblog.model import User,Post,Student



class Registration(FlaskForm):
    name = StringField('Name :', validators=[DataRequired()])
    email = StringField('Email : ',validators=[DataRequired(),Email()])
    password = PasswordField('Password :',validators=[DataRequired()])
    confirm_password = PasswordField('Confirm your password :',validators=[DataRequired(),EqualTo('password')])
    submit =SubmitField('Sign-up')
    def validate_username(self,name):
        user_name = User.query.filter_by(name=name.data).first()
        if user_name:
            raise ValidationError(f'This username is exist  ')
    def validate_email(self,email):
        user_email = User.query.filter_by(email=email.data).first()
        if user_email:
            raise ValidationError("This email is already register ! Please login")
class Login(FlaskForm):
    email = StringField('Email :', validators=[DataRequired()])
    password = PasswordField('Password :',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit =SubmitField('Log in')
class AssignmentPost(FlaskForm):
    CourseTitle   = StringField("Title :")
    CourseNo      = StringField("Course no :")
    DatePosted    = DateField("Posted at :" )
    Content       = StringField("Content :")
    MaximiumScore = IntegerField("Max Score : ")
    Remark        = StringField("Remark")
    Deadline      = DateField("Deadline at :")
    submit        =SubmitField('submit')
class ReportCard(FlaskForm):
    ID    = IntegerField("Student ID :",validators=[DataRequired()])
    Name  = StringField("Student Name",validators=[DataRequired()])
    Score = IntegerField("Score:",validators=[DataRequired()])
    Grade = SelectField(u'Grade:', choices=[('A','A'),('B','B'),('C','C'),('D','D'),('F','F'),('N/A','N/A')])
    submit =SubmitField('Add')
    def validate_id(self,ID):
        my_id = Student.query.filter_by(student_id=ID.data).first()
        if my_id:
            raise ValidationError('This student is exist  ')
