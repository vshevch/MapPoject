import model
from bottle import get, post, template, response, request, redirect, run
import json



@get('/')
def index():
    return template('input.html')


@get('/all')
def index():
    response.type = 'application/json'
    data = request.forms.get('term')
    return json.dumps({'data': model.allTerms()})


@post('/remove')
def index():
    data = request.forms.get('term')
    model.removeTerm(data)
    redirect('/all')


@post('/add')
def index():
    data = request.forms.get('term')
    model.addTerm(data)
    redirect('/all')


@get('/map')
def index():
    response.type = 'application/json'
    data = request.forms.get('term')
    global DB_Result
    DB_Result = model.allMap()
    return str(len(DB_Result))
    #return json.dumps({'data': model.allMap()})


run(reloader=True)
