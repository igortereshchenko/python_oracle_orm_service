from dao.db import OracleDb
import cx_Oracle

class UserHelper:

    def __init__(self):
        self.db = OracleDb()

    def getSkillData(self, skill_name=None):



        if not skill_name:
            query = 'select * from table(user_skillS.GetSkillData())'
        else:
            query = "select * from table(user_skillS.GetSkillData('{}'))".format(skill_name)

        result = self.db.execute(query)
        return result.fetchall()



    def getUserId(self, user_email, user_password):

        user_id = self.db.cursor.callfunc("USER_AUTH.GET_USER_ID", cx_Oracle.NATIVE_INT, [user_email, user_password])

        return user_id


    def newUser(self, USER_STUDYBOOK, USER_YEAR, USER_NAME, USER_EMAIL, USER_BIRTHDAY, USER_PASSWORD):

        cursor = self.db.cursor

        user_id = cursor.var(cx_Oracle.NATIVE_INT)
        status = cursor.var(cx_Oracle.STRING)

        cursor.callproc("USER_AUTH.NEW_USER", [user_id, status, USER_STUDYBOOK, USER_YEAR, USER_NAME, USER_EMAIL, USER_BIRTHDAY.upper(), USER_PASSWORD])

        return user_id.getvalue(), status.getvalue()



    def getUsers(self):

        return self.db.execute('SELECT * FROM "user"').fetchall()




if __name__ == "__main__":

    helper = UserHelper()

    print(helper.getSkillData('Java'))
    print(helper.getSkillData())

    print(helper.getUserId('PETRO@GMAIL.COM','222'))

    print(helper.newUser('KM5555', '10-OCT-17', 'Kate', 'KATE@GMAIL.COM', '21-OCT-97','555'))

    print(helper.getUsers())