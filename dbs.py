import sqlite3




def test_me():
    try: #everything you wanna do with your code
        db = sqlite3.connect("company.db")
        q = db.execute("SELECT * FROM users")
        users = q.fetchall()
        print(users)
    except Exception as ex: #handle things that can go wrong
        print(ex)
    finally: #will always run
        if "db" in locals(): db.close() #db er navn på variabel, locals er try blokken
        #dvs hvis der er en variabel kaldet db i try blokken udføres koden
        print("db closed")

test_me()

"""
#med context manager with, altid close connection
with sqlite3.connect("company.db") as db:
    q = db.execute("SELECT * FROM users")
    users = q.fetchall()
    print(users)
  """  

"""
#uden context manager
db = sqlite3.connect("company.db")
q = db.execute("SELECT * FROM users")
users = q.fetchall()
print(users)
db.close()
"""