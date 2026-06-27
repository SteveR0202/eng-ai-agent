from datasets import load_dataset, Dataset
import duckdb
from pathlib import Path

con = duckdb.connect("lakehouse.db")

out_file = Path("deliverables") / "hf_roundtrip_output.txt"
out_file.parent.mkdir(parents=True, exist_ok=True)

# ----------------------------
# 1. LOAD FROM HUB (INGESTION)
# ----------------------------
ds = load_dataset("Steve0208/coco-visdrone-gold")

df = ds["train"].to_pandas()

con.execute("CREATE OR REPLACE TABLE hf_ingested AS SELECT * FROM df")

# ----------------------------
# 2. PUSH BACK TO HUB
# ----------------------------
dataset = Dataset.from_pandas(df)
dataset.push_to_hub("Steve0208/coco-visdrone-gold")

# ----------------------------
# 3. SAVE PROOF OUTPUT
# ----------------------------
with open(out_file, "w") as f:
    f.write("HF ROUND TRIP SUCCESS\n\n")
    f.write(f"Rows ingested: {len(df)}\n")
    f.write("Dataset loaded and re-uploaded successfully\n")

print(f"Saved HF round-trip output to {out_file}")