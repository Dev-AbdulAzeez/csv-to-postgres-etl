# CSV to PostgreSQL ETL Pipeline

Python pipeline that extracts a sales CSV, cleans it with pandas, loads it into PostgreSQL with SQLAlchemy, and validates the load with SQL checks.

## Tools
Python, pandas, SQLAlchemy, PostgreSQL

## Results
- Extracted: 9,800 rows
- After cleaning: 9,799 rows
- Loaded into PostgreSQL: 9,799 rows
- Re-runnable: yes (the table is replaced on each run, no duplicates)

## Cleaning steps
- Standardised column names (lowercase, underscores)
- Removed empty rows and duplicate rows
- Converted dates and sales to proper types
- Dropped rows with an invalid date or sales value

## How to run
1. Install PostgreSQL and create a database called `etl_project`
2. `pip install -r requirements.txt`
3. Create a `.env` file with DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
4. Download the Superstore Sales CSV from Kaggle and save it as `data/raw/sales.csv`
5. `python etl.py`

## SQL validation
Queries are in `sql/checks.sql`. Screenshots are in `screenshots/`.

## Data source
Superstore Sales dataset, Kaggle: [https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting?resource=download]