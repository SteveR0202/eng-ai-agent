import boto3
from pathlib import Path

s3 = boto3.client(
    "s3",
    endpoint_url="http://rustfs:9000",
    aws_access_key_id="rustfsadmin",
    aws_secret_access_key="rustfsadmin"
)

bucket = "lakehouse"

for file in Path("coco/images").glob("*.jpg"):
    s3.upload_file(
        str(file),
        bucket,
        f"coco/images/{file.name}"
    )

print("Upload complete")