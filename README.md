# Lead Scoring with MySQL

This project analyzes lead quality using MySQL. It builds on the original Excel-based **Funnel KPI Case Study**, moving the data into a relational database for scalable analysis and deeper insights.

## 🚀 Goals

- Load and explore lead funnel data using SQL
- Identify high- vs. low-quality leads based on conversion rates
- Assign lead quality grades to improve prioritization

## 📁 Project Structure

```bash
├── data/
│ └── raw/ # Excel source files
├── scripts/
│ └── load_excel_to_mysql.py # Loads Excel data into MySQL
├── sql/
│ ├── 01_schema/
│ │ └── create_tables.sql # Table creation scripts
│ └── 02_queries/
│ └── explore_leads.sql # SQL queries for analysis
├── notebooks/ # (Optional) Jupyter notebooks
├── .env # Environment variables (excluded from Git)
├── environment.yml # Conda environment setup
├── requirements.txt # (Optional) pip-based dependencies
├── LICENSE
└── README.md
```

## 🗂️ Data

Source files are located in the `data/raw` directory and contain lead funnel metrics extracted from an Excel-based case study.

## 🛠️ Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/lead-scoring-mysql.git
   cd lead-scoring-mysql

## Create the environment

Using conda:

```bash
conda env create -f environment.yml
conda activate lead-scoring-mysql
```

## Configure environment variables

Create a .env file in the root directory with your MySQL credentials:

```bash
MYSQL_HOST=localhost
DB_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=yourpassword
MYSQL_DB=lead_scoring
```

## Create the database schema

```bash
mysql -u root -p lead_scoring < sql/01_schema/create_tables.sql
```

## Load data into MySQL

```bash
python scripts/load_excel_to_mysql.py
```

## Explore the data

```bash
mysql -u root -p lead_scoring < sql/02_queries/explore_leads.sql
```
