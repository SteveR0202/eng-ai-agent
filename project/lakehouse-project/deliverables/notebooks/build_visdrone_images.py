import pandas as pd
from pathlib import Path

rows = []

for file in Path("visdrone/images").glob("*.jpg"):
    rows.append({
        "image_id": file.name,
        "file_name": file.name,
        "width": None,
        "height": None,
        "s3_uri": f"s3://lakehouse/visdrone/images/{file.name}"
    })

df = pd.DataFrame(rows)

print(df.head())
print("Images:", len(df))