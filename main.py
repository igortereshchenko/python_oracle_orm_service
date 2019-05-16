from flask import Flask, render_template, request
from forms.userAUTO import userForm

from dao.userhelper import *
app = Flask(__name__)
app.secret_key = 'development key'




@app.route('/', methods=['GET', 'POST'])
def user():
    form = userForm()
    helper = UserHelper()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('userAUTO.html', form=form)
        else:
            user_id , status = helper.newUser(
                                            USER_STUDYBOOK=form.user_studybook.data,
                                            USER_BIRTHDAY=form.user_birthday.data.strftime("%d-%b-%y"),
                                            USER_EMAIL=form.user_email.data,
                                            USER_NAME=form.user_name.data,
                                            USER_PASSWORD=form.user_password.data,
                                            USER_YEAR=form.user_year.data.strftime("%d-%b-%y")
                                       )

            return "Status {} ID {}".format(status,user_id)


    return render_template('userAUTO.html', form=form, action='')


if __name__ == '__main__':
    app.run(debug=True)