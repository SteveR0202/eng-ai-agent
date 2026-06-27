import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("CREATE SCHEMA IF NOT EXISTS ml")

con.execute("""
CREATE OR REPLACE TABLE ml.dataset AS
SELECT
    i.s3_uri,
    a.dataset,
    a.category,
    a.x,
    a.y,
    a.w,
    a.h
FROM gold.annotations a
JOIN gold.images i
ON a.image_id = i.image_id
""")

print("ML dataset created")