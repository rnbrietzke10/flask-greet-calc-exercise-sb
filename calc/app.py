# Put your app in here.
from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/add')
def add_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{add(a,b)}"

@app.route('/sub')
def sub_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{sub(a,b)}"

@app.route('/mult')
def mult_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{mult(a,b)}"

@app.route('/div')
def div_route():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f"{div(a,b)}"

@app.route('/math/<operation>')
def all_in_one_route(operation):
    a = int(request.args['a'])
    b = int(request.args['b'])
    math_ops = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }
    return f"{math_ops[operation](a,b)}"
