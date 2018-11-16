
# Queries
addTerm = """INSERT INTO test (data) VALUES ('{}') RETURNING id;"""
removeTerm = """DELETE FROM test WHERE data = ('{}');"""
getAll = """SELECT data FROM test;"""
