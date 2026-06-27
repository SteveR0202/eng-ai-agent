# README.md

## Overview

This project implements a simple data lakehouse pipeline using the COCO and VisDrone datasets. The system uses DuckDB for analytics 
and RustFS for object storage. The pipeline follows a Raw → Silver → Gold architecture and includes data ingestion, cleaning, 
transformation, and export for machine learning use.

---

## Architecture

Raw Layer
- Stores original COCO and VisDrone images and annotations in RustFS
- Metadata is stored in DuckDB tables

Silver Layer
- Cleaned and filtered annotation data
- Removes invalid bounding boxes and prepares structured datasets

Gold Layer
- Aggregated analytical tables such as category counts and dataset summaries

---

## Requirements

- Docker and Docker Compose
- Python 3.10 or higher
- DuckDB
- pandas
- boto3
- datasets (Hugging Face)

Install Python dependencies:

bash

pip install duckdb pandas boto3 datasets