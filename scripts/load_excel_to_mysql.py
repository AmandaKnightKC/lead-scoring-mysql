import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

host = os.getenv("MYSQL_HOST")
port = int(os.getenv("DB_PORT"))
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DB")

# MySQL table column expectations
expected_columns = {
    "agent_data": [
        "agent_id", "agent_name", "agent_ramp", "start_date", "term_date", "login_email"
    ],
    "agent_quota": [
        "start_date", "end_date", "product_name", "ramp_month_code", "sales_quota"
    ],
    "marketing_leads": [
        "lead_id", "cost", "lead_source", "lead_creation_date", "contact_timestamp", "agent_id"
    ],
    "quotes": [
        "agent_name", "product_name", "created_date", "lead_id"
    ],
    "applications": [
        "agent_id", "product_name", "submitted_timestamp", "lead_id"
    ],
}

# Path to Excel and target sheets
excel_path = "data/raw/2025 BA Systems Analyst Project.xlsx"
sheet_names = list(expected_columns.keys())

# Connect to MySQL
conn = mysql.connector.connect(
    host=host, port=port, user=user, password=password, database=database
)
cursor = conn.cursor()

# Load sheets into a dictionary of DataFrames
sheets = pd.read_excel(excel_path, sheet_name=sheet_names, engine="openpyxl")

df_leads = None

for sheet_name, df in sheets.items():
    print(f"\nUploading sheet: {sheet_name}")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    print(f"Columns in `{sheet_name}` after cleaning: {list(df.columns)}")
    df = df.loc[:, ~df.columns.str.contains("^unnamed", case=False, na=False)]
    expected = expected_columns[sheet_name]
    df = df[[col for col in expected if col in df.columns]]
    df = df.where(pd.notnull(df), None)

    # Save marketing_leads for filtering other tables later
    if sheet_name == "marketing_leads":
        df_leads = df.copy()

    # Filter quotes and applications to ensure valid lead_id
    if sheet_name in ["quotes", "applications"] and df_leads is not None:
        valid_lead_ids = set(df_leads["lead_id"])
        df = df[df["lead_id"].isin(valid_lead_ids)]

    # Build and run insert query as before
    columns = ", ".join(df.columns)
    placeholders = ", ".join(["%s"] * len(df.columns))
    insert_query = f"INSERT INTO {sheet_name} ({columns}) VALUES ({placeholders})"

    success_count = 0
    for _, row in df.iterrows():
        values = []
        for col, val in row.items():
            if pd.isna(val):
                values.append(None)
            elif isinstance(val, str) and "T" in val and "Z" in val:
                try:
                    dt = datetime.fromisoformat(val.replace("Z", ""))
                    values.append(dt.strftime("%Y-%m-%d %H:%M:%S"))
                except Exception:
                    values.append(None)
            else:
                values.append(val)
        try:
            cursor.execute(insert_query, values)
            success_count += 1
        except Exception as e:
            print(f"❌ Error inserting row into `{sheet_name}`: {e}")
            print(row)

    conn.commit()
    print(f"✔ Inserted {success_count} rows into `{sheet_name}`")
    conn.commit()
    print(f"✔ Inserted {success_count} rows into `{sheet_name}`")

# Cleanup
cursor.close()
conn.close()
print("\n✅ All done.")
