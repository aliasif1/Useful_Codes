from flask import Flask,jsonify,request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

# conn = sqlite3.connect('database.db')
# print('Created and opened database successfully')

# conn.execute('CREATE TABLE Students (name TEXT, addr TEXT, city TEXT)')
# print('Students table created successfully')
# conn.close()

def addRecord():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO Students (name,addr,city) VALUES(?,?,?)',("Phillip","Indiranagar","Bangalore"))
    conn.commit()
    conn.close()

def getRecord():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    cur.execute('select * from Students')
    rows = cur.fetchall()
    print(rows)
    print(type(rows))

addRecord()
