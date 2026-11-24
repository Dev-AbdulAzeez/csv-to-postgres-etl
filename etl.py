import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

load_dotenv()

CSV_PATH = "data/raw/sales.csv"
TABLE_NAME = "sales_clean"


def extract(path):
    df = pd.read_csv(path, encoding="latin-1")
    print(f"Extracted {len(df)} rows")
    return df


def transform(df):
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[ -]", "_", regex=True)
    )
    df = df.dropna(how="all")
    check_cols = [c for c in df.columns if c != "row_id"]
    df = df.drop_duplicates(subset=check_cols)
    df["order_date"] = pd.to_datetime(df["order_date"], format="%d/%m/%Y", errors="coerce")
    df["ship_date"] = pd.to_datetime(df["ship_date"], format="%d/%m/%Y", errors="coerce")
    df["sales"] = pd.to_numeric(df["sales"], errors="coerce")
    df = df.dropna(subset=["order_date", "sales"])
    print(f"After cleaning: {len(df)} rows")
    return df


def load(df):
    url = URL.create(
        "postgresql+psycopg2",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD") or None,
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        database=os.getenv("DB_NAME"),
    )
    engine = create_engine(url)
    df.to_sql(TABLE_NAME, engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into {TABLE_NAME}")


if __name__ == "__main__":
    raw = extract(CSV_PATH)
    clean = transform(raw)
    load(clean)