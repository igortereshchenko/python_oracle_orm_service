from dao.credentials import username
from dao.db import OracleDb

db = OracleDb()

table_name = 'user'
table_owner = username

query = """
SELECT
    col.column_name,
    col.data_type,
    col.data_length
FROM
    sys.all_tab_columns col
    INNER JOIN sys.all_tables t 
    ON col.owner = t.owner AND col.table_name = t.table_name
WHERE
    col.owner = upper('{}')
    AND col.table_name = '{}'
""".format(table_owner,table_name)

result = db.execute(query)

# for column_name, data_type, data_lenght in result.fetchall():
#     print(column_name,data_type,data_lenght)


controls_mapping = \
    {
        "VARCHAR2":"StringField",
        "DATE":"DateField",
        "NUMBER":"IntegerField"
    }


class_file = """
from flask_wtf import Form
from wtforms import StringField,   SubmitField,  IntegerField, DateField
from flask import Flask, render_template, request, flash
from wtforms import validators, ValidationError

class {}Form(Form):
""".format(table_name.upper())


form_file="""
<form action = "/{}" method = post>
         <fieldset>
""".format(table_name.lower())


for column_name, data_type, data_lenght in result.fetchall():
    class_file+="    {} = {}('{}: ')\n".format(column_name, controls_mapping[data_type], column_name)

    form_file+="    {{ form.{}.label }} {{ form.{} }} <br/>\n".format(column_name.lower(), column_name.lower())


class_file+="    submit = SubmitField('Submit')"

form_file+="""
        {{ form.submit }}
        </fieldset>
</form>         
"""


with open("../forms/{}AUTO.py".format(table_name), "w") as file:
    file.write(class_file)
    file.close()

with open("../templates/{}formAUTO.html".format(table_name.lower()), "w") as file:
    file.write(form_file)
    file.close()
