from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

# just imports various validators to fields and creates forms

class SignUpForm(FlaskForm):
    name = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired(), Email(message="not a valid email")])
    mobile = IntegerField()
    country = StringField(validators=[DataRequired()])
    newsletter = BooleanField('Weekly Digest')
    submit = SubmitField()

