import sqlite3
from pathlib import Path

# --- Build correct paths based on script location ---
BASE_DIR = Path(__file__).resolve().parent.parent  # go up from /src

DB_PATH = BASE_DIR / "clinic_simple.db"
CSV_PATH = "./data/patients.csv"
SCHEMA_PATH = BASE_DIR / "sql" / "schema.sql"

def main():
    # Read schema
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Create DB
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)

    print(f"Created database at: {DB_PATH}")

if __name__ == "__main__":
    main()