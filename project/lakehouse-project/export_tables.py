import duckdb

con = duckdb.connect("lakehouse.db")

exports = [
    ("raw.coco_images", "coco_images.csv"),
    ("raw.coco_annotations", "coco_annotations.csv"),
    ("raw.visdrone_images", "visdrone_images.csv"),
    ("raw.visdrone_annotations", "visdrone_annotations.csv"),

    ("silver.coco_images", "silver_coco_images.csv"),
    ("silver.coco_annotations", "silver_coco_annotations.csv"),
    ("silver.visdrone_images", "silver_visdrone_images.csv"),
    ("silver.visdrone_annotations", "silver_visdrone_annotations.csv"),

    ("gold.images", "gold_images.csv"),
    ("gold.annotations", "gold_annotations.csv"),
]

for table, file in exports:
    try:
        con.execute(f"""
        COPY {table}
        TO 'deliverables/csv_exports/{file}'
        (HEADER, DELIMITER ',');
        """)
        print(f"Exported {file}")
    except Exception as e:
        print(f"Skipped {table}: {e}")