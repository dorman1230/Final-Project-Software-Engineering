import sqlite3


class Users:
    """Creates database with users table includes:
       create query
       insert query
       select query
    """

    def __init__(self, tablename="users", userId="userId", username="username", password="password"):
        self.__tablename = tablename
        self.__userId = userId
        self.__password = password
        self.__username = username
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        query_str = "CREATE TABLE IF NOT EXISTS " + tablename + "(" + self.__userId + " " + \
                    " INTEGER PRIMARY KEY AUTOINCREMENT ,"
        query_str += " " + self.__username + " TEXT    NOT NULL ,"
        query_str += " " + self.__password + " TEXT    NOT NULL );"

        # conn.execute("Create table users")
        conn.execute(query_str)
        print("Table created successfully")
        conn.commit()
        conn.close()

    def __str__(self):
        return "table  name is ", self.__tablename

    def get_table_name(self):
        return self.__tablename

    def insert_user(self, username, password):
        conn = sqlite3.connect('test.db')
        insert_query = "INSERT INTO " + self.__tablename + " (" + self.__username + "," + self.__password + ") VALUES " \
                                                                                                            "(" + "'" + username + "'" + "," + "'" + password + "'" + ");"
        print(insert_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()
        print("Record created successfully")

    def select_user_by_id(self, userId):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "select userId, username, password from " + self.__tablename + " where " + self.__userId + " = " + str(userId) + ";"

        cursor = conn.execute(str1)
        for row in cursor:
            print("userId = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])

        print("Operation done successfully")
        conn.close()

    def remove_user(self, userId):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "delete from " + self.__tablename + " where " + self.__userId + " = '" + str(userId) + "';"
        conn.execute(str1)
        conn.commit()
        print("SUCCESS: Deleted user with ID: " + str(userId))
        conn.close()

    def update_password(self, userId, password):
        conn = sqlite3.connect('test.db')
        print("Opened database successfully")
        str1 = "update " + self.__tablename + " set " + self.__password + " = '" + str(password) + "' where " + self.__userId + " = '" + str(userId) + "';"
        conn.execute(str1)
        conn.commit()
        print("SUCCESS: Updated password for user with ID: " + str(userId))
        conn.close()


u = Users()
u.insert_user("amit", "password1")
u.insert_user("bob", "12345")
u.insert_user("omer", "biglongpassword12345")

u.remove_user(2)

u.update_password(1, "newpassword")