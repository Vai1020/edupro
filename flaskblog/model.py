from datetime import datetime
from flaskblog import db,login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name_of_school=db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('quiz', backref='questions', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.name_of_school}')"

class quiz(db.Model):
    qno = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    Class=db.Column(db.String(50), nullable=False)
    Subject_Name=db.Column(db.String(500), nullable=False)
    question = db.Column(db.String(500), nullable=False)
    option_1 = db.Column(db.String(200), nullable=False)
    option_2 = db.Column(db.String(200), nullable=False)
    option_3 = db.Column(db.String(200), nullable=False)
    option_4 = db.Column(db.String(200), nullable=False)
    correct_answer= db.Column(db.String(200), nullable=False)
   
    def __repr__(self):
        return f"quiz('{self.question}', '{self.Subject}', '{self.Class}')"

class ans(db.Model):
    sno = db.Column(db.Integer, primary_key=True,autoincrement=True)
    question_id=db.Column(db.Integer, db.ForeignKey('quiz.qno'))
    roll_no=db.Column(db.Integer,)
    option = db.Column(db.String(200),default=False)
    right=db.Column(db.Integer,default=None)
    marks=db.Column(db.Integer,)
    #db.UniqueConstraint(roll_no)

    def __repr__(self) -> str:
        return f"ans('{self.question}', '{self.roll_no}', '{self.option}')"
