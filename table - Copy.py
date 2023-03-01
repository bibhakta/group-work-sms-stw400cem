import sqlite3

connection=sqlite3.connect('registers_std.db')
exe=connection.cursor()
exe.execute("CREATE TABLE Account(FirstName text, LastName text, Phone int, Email text, Password text, ConfirmPass text, status boolean)")
connection.commit()
connection.close()