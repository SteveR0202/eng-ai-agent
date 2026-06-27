import duckdb

con = duckdb.connect()

con.execute("INSTALL ducklake; LOAD ducklake;")

con.execute(open("sql/00_attach.sql").read())

print(
    con.sql(
        "SELECT * FROM lake.snapshots()"
    )
)
