import duckdb
import os
from pathlib import Path

con = duckdb.connect("lakehouse.db")

# Create fragment table
con.execute("""
CREATE TABLE IF NOT EXISTS raw.visdrone_fragments (
    fragment_id INTEGER,
    video_id VARCHAR,
    frame_start INTEGER,
    frame_end INTEGER,
    s3_uri VARCHAR
)
""")

# Path to VisDrone videos or frame folders
base_path = Path("visdrone")

rows = []
fragment_id = 1

# If dataset is frame-based (most VisDrone datasets are)
for video_folder in base_path.iterdir():
    if video_folder.is_dir():

        video_id = video_folder.name

        frames = sorted(video_folder.glob("*.jpg"))

        # split into fragments of 50 frames
        chunk_size = 50

        for i in range(0, len(frames), chunk_size):
            chunk = frames[i:i + chunk_size]

            if len(chunk) == 0:
                continue

            start_frame = i
            end_frame = i + len(chunk) - 1

            # fake S3 URI (or real if uploaded)
            s3_uri = f"s3://lakehouse/visdrone/{video_id}/fragment_{fragment_id}.jpg"

            rows.append((
                fragment_id,
                video_id,
                start_frame,
                end_frame,
                s3_uri
            ))

            fragment_id += 1

# Insert into DuckDB
con.executemany("""
INSERT INTO raw.visdrone_fragments
VALUES (?, ?, ?, ?, ?)
""", rows)

print(f"Inserted {len(rows)} VisDrone fragments")