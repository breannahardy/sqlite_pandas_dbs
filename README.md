## Single Table Patient Roster
This project demonstrates a basic workflow using SQLite, Python, Pandas, and SQLAlchemy to build, populate, and query a simple patient database. 

## Steps to Create Database
-  Create folder structure
```
sqlite_pandas_dbs
├─ data/
│  └─ patients.csv
├─ sql/
│  ├─ schema.sql
│  └─ analysis.sql
├─ src/
│  ├─ create_db.py         
│  └─ import_csv.py        
├─ clinic_simple.db        
├─ requirements.txt
└─ README.md
```
- Install dependencies:
  ```bash
   pip install -r requirements.txt

-  Describe structure of patients table, including column names and data types. This defines the schema `sql/schema.sql`
- Create database `src/create_db.py` by using sqlite3 to read schema file and generate database `clinic_simple.db`
- Load `patients.csv` onto table by running `import_csv.py` using pandas and SQLAlchemy 
- Open DB Browser to run queries `sql/analysis.sql`

## Queries on DB Browser
A. Row Count
- There are 500 records in the patient table
  
  <img width="541" height="599" alt="A  Row Count" src="https://github.com/user-attachments/assets/b5c7e87c-f4eb-43df-ac87-433cab145fe9" />

B. Top Primary Diagnoses by Count
- The top diagnoses is I10 with 81 patients 

<img width="551" height="791" alt="B) Top Primary Diagnoses by count" src="https://github.com/user-attachments/assets/557490c0-9764-4e7a-bdc9-e34115b6a42f" />

C. Office-visit CPTs since Jan 1, 2025 (CPT codes starting with 992)
- 94 patients have had a visit from Jan 1, 2025.

<img width="554" height="802" alt="C) Office Visit CPTs" src="https://github.com/user-attachments/assets/0eb55a5a-b562-4feb-a0bb-99298752a610" />

D. Age (approx) at the latest visit for 5 oldest patients
- Below shows the age, DOB and visit date for the 5 oldest patients. Oldest age for these five patients is approx 85 yrs old.

  <img width="558" height="549" alt="D) Age of Oldest Patients" src="https://github.com/user-attachments/assets/23b85276-70ac-4a00-852a-765ebdb7c7eb" />

E. Data Quality Check- Blank Codes
- There are no blank codes shown in the table people, meaning every patient is assigned a diagnoses

  <img width="563" height="547" alt="E) Data Quality Check" src="https://github.com/user-attachments/assets/531d7446-a63d-4273-a3a0-940ae39e818f" />
