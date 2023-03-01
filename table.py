import sqlite3

connection=sqlite3.connect('register_std.db')
exe=connection.cursor()
exe.execute("CREATE TABLE Account(FirstName text, LastName text, Phone int, Email text, Password text, ConfirmPass text)")
connection.commit()
connection.close()