import duckdb
import pandas as pd
from pathlib import Path

con = duckdb.connect("lakehouse.db")

images = []

for f in Path("visdrone/images").glob("*.jpg"):
    images.append({
        "image_id": f.name,
        "file_name": f.name,
        "width": None,
        "height": None,
        "s3_uri": f"s3://lakehouse/visdrone/images/{f.name}"
    })

images_df = pd.DataFrame(images)

con.register("vis_images", images_df)

con.execute("""
INSERT INTO raw.visdrone_images
SELECT * FROM vis_images
""")

rows = []
annotation_id = 0

for file in Path("visdrone/annotations").glob("*.txt"):
    image_id = file.stem + ".jpg"

    with open(file) as f:
        for line in f:
            p = line.strip().split(",")

            rows.append({
                "annotation_id": annotation_id,
                "image_id": image_id,
                "category": int(p[5]),
                "bbox_left": float(p[0]),
                "bbox_top": float(p[1]),
                "bbox_width": float(p[2]),
                "bbox_height": float(p[3])
            })

            annotation_id += 1

ann_df = pd.DataFrame(rows)

con.register("vis_ann", ann_df)

con.execute("""
INSERT INTO raw.visdrone_annotations
SELECT * FROM vis_ann
""")

print("VisDrone fully loaded")
