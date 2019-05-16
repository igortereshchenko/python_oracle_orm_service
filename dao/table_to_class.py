from dao.credentials import username
from dao.db import OracleDb

db = OracleDb()

table_name = 'user'
table_owner = username

query = """
SELECT
    col.column_name,
    col.data_type,
    col.nullable
FROM
    sys.all_tab_columns col
    INNER JOIN sys.all_tables t 
    ON col.owner = t.owner AND col.table_name = t.table_name
WHERE
    col.owner = upper('{0}')
    AND col.table_name = '{1}'
""".format(table_owner,table_name)

result = db.execute(query)


controls_mapping = \
    {
        "VARCHAR2":"StringField",
        "DATE":"DateField",
        "NUMBER":"IntegerField",
        "CHAR": "StringField",
    }



class_fields = ""
form_fields = ""

for column_name, data_type, nullable in result.fetchall():
    if nullable=='Y':
        data_required = ""
    else:
        data_required = ",[validators.DataRequired('Please enter {0}.')]".format(column_name.lower())

    class_fields +="    {0} = {1}('{2}: '".format(column_name.lower(), controls_mapping[data_type], column_name.lower()) +data_required+ ")\n"


    form_fields +=\
    """
    <div class="form-group">
        {{{{ form.{0}.label }}}} 
        {{{{ form.{1}(class_="form-control") }}}} 
    </div>\n""".format(column_name.lower(), column_name.lower())






with open("file_templates/wtf_form", "r") as file:
    class_file = file.read()
    class_file = class_file.replace('$FIELDS$',class_fields)
    class_file = class_file.replace('$CLASSNAME$', table_name.lower())


    class_file = class_file.replace('$KEY$', table_name.lower()+"_id")

    file.close()

    with open("../forms/{}AUTO.py".format(table_name.lower()), "w") as file:
         file.write(class_file)
         file.close()




with open("file_templates/html_form", "r") as file:
    html_file = file.read()
    html_file = html_file.replace('$FIELDS$',form_fields)
    html_file = html_file.replace('$FORMNAME$', "Form for {0}".format(table_name))
    file.close()

    with open("../templates/{}AUTO.html".format(table_name.lower()), "w") as file:
        file.write(html_file)
        file.close()
