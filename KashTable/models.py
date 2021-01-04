from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from sqlalchemy_utils import ChoiceType, EmailType
from KashTable import db, login_manager


"""


For more information on declaring models: 
    - https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
    - https://docs.sqlalchemy.org/en/14/core/type_basics.html


"""

AVAILABLE_USER_TYPES = [
    (u'admin', u'Admin'),
    (u'client', u'Client'),
]  

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):    
    id = db.Column(db.Integer, primary_key=True)    
    # use a regular string field, for which we can specify a list of available 
    # choices later on
    type = db.Column(db.String(100), nullable=True, default='client') 
    sqla_utils_choice_field = db.Column(ChoiceType(AVAILABLE_USER_TYPES), nullable=True)  
    company_name = db.Column(db.String(20), nullable=False)
    street = db.Column(db.String(128), nullable=False)
    postcode = db.Column(db.String(7), nullable=False)    
    city = db.Column(db.String(128), nullable=False)
    country = db.Column(db.String(128), nullable=False)
    siren = db.Column(db.String(20), nullable=False)    

    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(EmailType, unique=True, nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='blank.jpg')

    bundle = db.Column(db.Integer, nullable=False)
    activated = db.Column(db.Boolean, nullable=False, default=True)
    
    password = db.Column(db.String(60), nullable=False)    
    file = db.relationship('File', backref='client', lazy=True)    
    
    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
        
    def __str__(self):
        return "{}, {}".format(
                self.company_name, 
                self.email
            )
    
    def __repr__(self):
        return "User('{}', '{}', '{}')".format(
                self.user_id,
                self.company_name,
                self.email,
                self.bundle,
                self.activated
            )

  
class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    doc = db.Column(db.PickleType(), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id))
    user = db.relationship(User, foreign_keys=[user_id], backref='files')
    
    def __repr__(self):
        return "User('{}', '{}', '{}')".format(
                self.user_id,
                self.date,
                self.doc
            )