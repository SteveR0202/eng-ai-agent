import duckdb
from pathlib import Path

con = duckdb.connect("lakehouse.db")

out_dir = Path("deliverables")
out_dir.mkdir(parents=True, exist_ok=True)

output_file = out_dir / "versioning_output.txt"

with open(output_file, "w") as f:

    f.write("VERSIONING DEMO (DUCKDB COMPATIBLE)\n\n")

    baseline = con.execute("""
    SELECT COUNT(*) FROM gold.category_counts
    """).fetchone()

    f.write(f"BASELINE COUNT: {baseline}\n")

    con.execute("""
    INSERT INTO gold.category_counts VALUES (999999, 1)
    """)

    changed = con.execute("""
    SELECT COUNT(*) FROM gold.category_counts
    """).fetchone()

    f.write(f"AFTER INSERT COUNT: {changed}\n")

    con.execute("""
    DELETE FROM gold.category_counts
    WHERE category_id = 999999
    """)

    rolled_back = con.execute("""
    SELECT COUNT(*) FROM gold.category_counts
    """).fetchone()

    f.write(f"AFTER ROLLBACK COUNT: {rolled_back}\n")

    f.write("\nNOTE:\n")
    f.write("Versioning simulated using insert/delete state changes\n")

print("Saved to deliverables/versioning_output.txt")