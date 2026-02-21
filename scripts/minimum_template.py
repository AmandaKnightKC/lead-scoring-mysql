import os
import pandas as pd
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("DB_PORT", "3306")),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DB"),
)
cursor = conn.cursor()

excel_path = "data/raw/your_file.xlsx"
sheets = pd.read_excel(excel_path, sheet_name=["sheet1", "sheet2"], engine="openpyxl")

for name, df in sheets.items():
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df = df.where(pd.notnull(df), None)
    # insert into mysql here