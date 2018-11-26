import psycopg2
import queries

# Not sure how to use getDB
def getDB():
    db = psycopg2.connect(
        host="localhost",
        database="map_project",
        user="vladshev",
        password="root",
    )
    db.autocommit = True
    return db.cursor()

def addTerm(t):
    db = getDB()
    result = db.execute(queries.addTerm.format(t))
    return result


def removeTerm(t):
    db = getDB()
    result = db.execute(queries.removeTerm.format(t))
    return result


def allTerms():
    db = getDB()
    db.execute(queries.getAll)
    return db.fetchall()

def allMap():
    db = getDB()
    db.execute(queries.getMap)
    return db.fetchall()
