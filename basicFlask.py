from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
import json
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True


books = [
    {
        'num':1,
        'name':'book1'
    },
    {
        'num':2,
        'name':'book2'
    },
    {
        'num':3,
        'name':'book3'
    }
    ]

@app.route("/",methods = ["GET"])
@cross_origin(origin='*')
def Home():
    return '<h1> Hello </h1>'

@app.route("/books",methods = ["GET","POST"])
@cross_origin(origin='*')
def GetBooks():
    print(request.data)
    print(request.headers['Content-Type-Custom'])
    return jsonify(books)

@app.route("/book",methods = ["GET"])
@cross_origin(origin='*')
def GetBook():
    if ('x' in request.args):
        x = int(request.args['x'])
    else:
        return('Bad request')
    book = []
    for b in books:
        if b['num'] == x:
            book.append(b)
    return jsonify(book)




if (__name__) == '__main__':
    app.run(debug=True)
