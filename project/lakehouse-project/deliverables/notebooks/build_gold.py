import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("CREATE SCHEMA IF NOT EXISTS gold")

con.execute("""
CREATE OR REPLACE TABLE gold.annotations AS

SELECT
    'coco' AS dataset,
    image_id,
    category_id AS category,
    bbox_x AS x,
    bbox_y AS y,
    bbox_width AS w,
    bbox_height AS h
FROM silver.coco_annotations

UNION ALL

SELECT
    'visdrone' AS dataset,
    image_id,
    category AS category,
    bbox_left AS x,
    bbox_top AS y,
    bbox_width AS w,
    bbox_height AS h
FROM silver.visdrone_annotations
""")

con.execute("""
CREATE OR REPLACE TABLE gold.images AS

SELECT
    'coco' AS dataset,
    image_id,
    file_name,
    s3_uri
FROM silver.coco_images

UNION ALL

SELECT
    'visdrone' AS dataset,
    image_id,
    file_name,
    s3_uri
FROM silver.visdrone_images
""")

print("Gold layer created")