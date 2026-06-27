import pandas as pd
from pathlib import Path

rows = []

annotation_path = Path("visdrone/annotations")

for file in annotation_path.glob("*.txt"):
    image_id = file.stem + ".jpg"

    with open(file) as f:
        for line in f:
            parts = line.strip().split(",")

            rows.append({
                "image_id": image_id,
                "bbox_left": float(parts[0]),
                "bbox_top": float(parts[1]),
                "bbox_width": float(parts[2]),
                "bbox_height": float(parts[3]),
                "category": int(parts[5])
            })

df = pd.DataFrame(rows)

print(df.head())
print("Annotations loaded:", len(df))
