# read the source (excel)
import pandas as pd

df = pd.read_excel("data/raw/leads.xlsx", sheet_name="leads")

# basic cleanup
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
df = df.drop_duplicates()

# Connect to MySQL using environment variables

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(
    f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@"
    f"{os.getenv('DB_HOST','localhost')}:{os.getenv('DB_PORT','3306')}/"
    f"{os.getenv('DB_NAME')}"
)
# read env vars for DB connection (user, pass, host, port
host = os.getenv("MYSQL_HOST")
port = int(os.getenv("DB_PORT"))
user = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
database = os.getenv("MYSQL_DB")

# Connect to MySQL
conn = mysql.connector.connect(
    host=host, port=port, user=user, password=password, database=database
)
cursor = conn.cursor()

# Load to a table (replace or append)

df.to_sql("leads_raw", con=engine, if_exists="replace", index=False)

# Why use .env? (secrets + portability)
# Why normalize column names? (consistent SQL + fewer bugs)
# Why staging table (*_raw)? (debugging + reproducibility)
# Why chunk inserts? (speed + memory)
# Why replace vs append? (rebuild vs incremental loads)
