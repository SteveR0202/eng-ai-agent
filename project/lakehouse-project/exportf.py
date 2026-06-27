import duckdb

con = duckdb.connect("lakehouse.db")

con.execute("""
COPY raw.visdrone_fragments
TO 'deliverables/csv_exports/visdrone_fragments.csv'
(HEADER, DELIMITER ',');
""")