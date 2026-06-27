import boto3
from pathlib import Path

s3 = boto3.client(
    "s3",
    endpoint_url="http://rustfs:9000",
    aws_access_key_id="rustfsadmin",
    aws_secret_access_key="rustfsadmin"
)

bucket = "lakehouse"

image_path = Path("visdrone/images")

for file in image_path.glob("*.jpg"):
    s3.upload_file(
        str(file),
        bucket,
        f"visdrone/images/{file.name}"
    )

print("VisDrone images uploaded")