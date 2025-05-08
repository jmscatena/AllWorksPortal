from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, EmailField, SelectField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    """Form for website visitors to contact the company"""
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=2, max=100, message='Name must be between 2 and 100 characters')
    ])
    
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(message='Please enter a valid email address')
    ])
    
    subject = StringField('Subject', validators=[
        DataRequired(),
        Length(min=3, max=200, message='Subject must be between 3 and 200 characters')
    ])
    
    inquiry_type = SelectField('Inquiry Type', choices=[
        ('', 'Select an inquiry type'),
        ('general', 'General Inquiry'),
        ('project', 'Project Information'),
        ('course', 'Course Information'),
        ('training', 'Training Program'),
        ('publication', 'Publications Request'),
        ('partnership', 'Partnership Opportunity'),
        ('other', 'Other')
    ], validators=[DataRequired(message='Please select an inquiry type')])
    
    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(min=10, max=2000, message='Message must be between 10 and 2000 characters')
    ])
