import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

con.execute("""
CREATE TABLE raw.visdrone_images (
    image_id VARCHAR,
    file_name VARCHAR,
    width INTEGER,
    height INTEGER,
    s3_uri VARCHAR
)
""")

con.execute("""
CREATE TABLE raw.visdrone_annotations (
    annotation_id BIGINT,
    image_id VARCHAR,
    category INTEGER,
    bbox_left DOUBLE,
    bbox_top DOUBLE,
    bbox_width DOUBLE,
    bbox_height DOUBLE
)
""")

print("Tables created")
