import json
import pandas as pd

with open("coco/annotations/instances_train2017.json") as f:
    coco = json.load(f)

images_df = pd.DataFrame(coco["images"])
annotations_df = pd.DataFrame(coco["annotations"])

print("Images:", len(images_df))
print("Annotations:", len(annotations_df))
