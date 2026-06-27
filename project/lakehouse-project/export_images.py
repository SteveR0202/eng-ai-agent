import duckdb

con = duckdb.connect("lakehouse.db")

tables = [
    ("silver.coco_images", "silver_coco_images.csv"),
    ("silver.visdrone_images", "silver_visdrone_images.csv"),

]

for table, filename in tables:
    try:
        con.execute(f"""
        COPY {table}
        TO 'deliverables/{filename}'
        (HEADER, DELIMITER ',');
        """)
        print(f"Exported {filename}")
    except Exception as e:
        print(f"Skipped {table}: {e}")