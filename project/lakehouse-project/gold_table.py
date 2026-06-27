import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("""
CREATE TABLE gold.category_counts AS
SELECT
    category_id,
    COUNT(*) AS total_objects
FROM silver.coco_annotations
GROUP BY category_id;
""")

print("Created gold.category_counts")