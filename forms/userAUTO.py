
from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError

class USERForm(Form):
    USER_PASSWORD = StringField('USER_PASSWORD: ')
    USER_BIRTHDAY = DateField('USER_BIRTHDAY: ')
    USER_EMAIL = StringField('USER_EMAIL: ')
    USER_NAME = StringField('USER_NAME: ')
    USER_YEAR = DateField('USER_YEAR: ')
    USER_STUDYBOOK = StringField('USER_STUDYBOOK: ')
    USER_ID = IntegerField('USER_ID: ')
    submit = SubmitField('Submit')