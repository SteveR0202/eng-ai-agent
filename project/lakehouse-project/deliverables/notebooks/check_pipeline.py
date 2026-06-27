import duckdb

con = duckdb.connect("lakehouse.db")

print("RAW:")
print(con.execute("SELECT COUNT(*) FROM raw.coco_annotations").fetchall())
print(con.execute("SELECT COUNT(*) FROM raw.visdrone_annotations").fetchall())

print("SILVER:")
print(con.execute("SELECT COUNT(*) FROM silver.coco_annotations").fetchall())
print(con.execute("SELECT COUNT(*) FROM silver.visdrone_annotations").fetchall())

print("GOLD:")
print(con.execute("SELECT COUNT(*) FROM gold.annotations").fetchall())