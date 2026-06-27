import duckdb
from pathlib import Path

con = duckdb.connect("lakehouse.db")

out_file = Path("deliverables") / "fragment_query_output.txt"

# Ensure folder exists
out_file.parent.mkdir(parents=True, exist_ok=True)

# Query selected fragments
result = con.execute("""
SELECT *
FROM raw.visdrone_fragments
WHERE frame_start <= 100
AND frame_end >= 50;
""").df()

# Materialize selected fragments
con.execute("""
CREATE TABLE IF NOT EXISTS silver.selected_visdrone_fragments AS
SELECT *
FROM raw.visdrone_fragments
WHERE frame_start <= 100
AND frame_end >= 50;
""")

# Save proof output
with open(out_file, "w") as f:
    f.write("VISDRONE FRAGMENT QUERY OUTPUT\n\n")
    f.write(result.to_string())

print(f"Saved fragment query output to {out_file}")