import duckdb

con = duckdb.connect()

sql = open("sql/00_attach.sql").read()

con.execute(sql)

print("Connected!")