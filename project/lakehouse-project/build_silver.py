import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("CREATE SCHEMA IF NOT EXISTS silver")

# ---------------- COCO CLEAN ----------------
con.execute("""
CREATE OR REPLACE TABLE silver.coco_annotations AS
SELECT *
FROM raw.coco_annotations
WHERE bbox_width > 0
AND bbox_height > 0
""")

con.execute("""
CREATE OR REPLACE TABLE silver.coco_images AS
SELECT *
FROM raw.coco_images
""")

# ---------------- VISDRONE CLEAN ----------------
con.execute("""
CREATE OR REPLACE TABLE silver.visdrone_annotations AS
SELECT *
FROM raw.visdrone_annotations
WHERE bbox_width > 0
AND bbox_height > 0
""")

con.execute("""
CREATE OR REPLACE TABLE silver.visdrone_images AS
SELECT *
FROM raw.visdrone_images
""")

print("Silver layer created")