import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("DROP TABLE IF EXISTS raw.visdrone_images")
con.execute("DROP TABLE IF EXISTS raw.visdrone_annotations")

print("VisDrone tables dropped")