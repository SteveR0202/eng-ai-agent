from datasets import Dataset
import duckdb

con = duckdb.connect("lakehouse.db")

df = con.execute("""
SELECT *
FROM gold.annotations
""").df()

dataset = Dataset.from_pandas(df)

dataset.push_to_hub(
    "Steve0208/coco-visdrone-gold"
)

print("Uploaded to Hugging Face")