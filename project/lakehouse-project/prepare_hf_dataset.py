import duckdb

con = duckdb.connect("lakehouse.db")

df = con.execute("""
SELECT
    dataset,
    image_id,
    category,
    x,
    y,
    w,
    h
FROM gold.annotations
""").df()

print(df.head())
print(len(df))