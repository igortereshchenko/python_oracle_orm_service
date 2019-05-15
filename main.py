from flask import Flask, render_template, request
from forms.user import UserForm

from dao.userhelper import *
app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def user():
    form = UserForm()

    helper = UserHelper()
    allUsers = helper.getUsers()

    if request.method == 'POST':
        if form.validate() == False:
            return render_template('user.html', form=form, users = allUsers)
        else:
            user_id , status = helper.newUser(
                                            USER_STUDYBOOK=request.form["studybook"],
                                            USER_BIRTHDAY=request.form["birthday"],
                                            USER_EMAIL=request.form["email"],
                                            USER_NAME=request.form["name"],
                                            USER_PASSWORD=request.form["password"],
                                            USER_YEAR=request.form["study_year"]
                                       )

            return "Status {} ID {}".format(status,user_id)


    return render_template('user.html', form=form, users = allUsers)


if __name__ == '__main__':
    app.run(debug=True)