from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError
from dao.db import OracleDb

class userForm(Form):

    user_password = StringField('user_password: ')
    user_birthday = DateField('user_birthday: ',[validators.DataRequired('Please enter user_birthday.')])
    user_email = StringField('user_email: ')
    user_name = StringField('user_name: ',[validators.DataRequired('Please enter user_name.')])
    user_year = DateField('user_year: ',[validators.DataRequired('Please enter user_year.')])
    user_studybook = StringField('user_studybook: ',[validators.DataRequired('Please enter user_studybook.')])
    user_id = IntegerField('user_id: ',[validators.DataRequired('Please enter user_id.')])


    submit = SubmitField('Submit')


    def delete(self):
        db = OracleDb()
        query = "DELETE FROM user WHERE {0} = {1}".format('user_id', self.user_id.data)

        db.execute(query)
