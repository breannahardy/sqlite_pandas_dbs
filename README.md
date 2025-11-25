## Single Table Patient Roster
This project demonstrates a basic ETL workflow using SQLite, Python, Pandas, and SQLAlchemy to build, populate, and query a simple patient database. 

## Steps to Create Database
-  Create folder structure
'sqlite_pandas_dbs/
├─ data/
│   └─ patients.csv
├─ sql/
│   ├─ schema.sql
│   └─ analysis.sql
├─ src/
│   ├─ create_db.py
│   └─ import_csv.py
├─ clinic_simple.db        # Automatically created after running create_db.py
└─ README.md '
- Install dependencies: pip install pandas sqlalchemy
-  Describe structure of patients table, including column names and data types. This defines the schema 'sql/schema.sql'
- Create database 'src/create_db.py by using sqlite3 to read schema file and generate database 'clinic_simple.db'
- Load 'patients.csv' onto table by running 'import_csv.py' using pandas and SQLAlchemy 
- Open DB Browser to run queries 'sql/analysis.sql'

## Queries on DB Browser
A. Row Count
- There are 500 records in the patient table 
