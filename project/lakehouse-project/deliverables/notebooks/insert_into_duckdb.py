import duckdb
import json
import pandas as pd

con = duckdb.connect("lakehouse.db")

with open("coco/annotations/instances_train2017.json") as f:
    coco = json.load(f)

images_df = pd.DataFrame(coco["images"])

images_df = images_df[["id", "file_name", "width", "height"]]

images_df = images_df.rename(columns={"id": "image_id"})

images_df["s3_uri"] = None

con.register("images_df", images_df)

con.execute("""
INSERT INTO raw.coco_images
SELECT * FROM images_df
""")

print("Inserted COCO images safely")
