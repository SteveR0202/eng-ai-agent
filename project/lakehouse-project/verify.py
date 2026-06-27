import duckdb

con = duckdb.connect()

con.execute(open("sql/00_attach.sql").read())

print(
    con.sql(
        "SELECT COUNT(*) FROM raw.ag_news"
    )
)