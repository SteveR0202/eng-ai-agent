#!/bin/bash

set -e

echo "Starting full rebuild..."

python3 reset_vis.py || true

python3 create_tables.py

python3 insert_into_duckdb.py
python3 insert_visdrone_into_duckdb.py

python3 build_silver.py
python3 build_gold.py
python3 check_pipeline.py
python3 build_ml_dataset.py

python3 prepare_hf_dataset.py
python3 push_hf.py

echo "Pipeline complete"
