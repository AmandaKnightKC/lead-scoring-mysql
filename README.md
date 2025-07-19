# Lead Scoring with MySQL

This project analyzes lead quality using MySQL. It builds on the original Excel-based [Funnel KPI Case Study] and shifts the data into a relational database for more scalable analysis.

## Goals

- Load and explore lead funnel data using SQL.
- Identify high- vs. low-quality leads based on conversion rates.
- Assign lead quality grades for better prioritization.

## Data

Source data is located in the `data/raw` folder and includes lead funnel metrics in Excel format.

## Getting Started

1. Clone the repo:

   ```bash
   git clone https://github.com/YOUR_USERNAME/lead-scoring-mysql.git
   cd lead-scoring-mysql

# Run schema creation

```sql
mysql -u user -p database_name < sql/schema/add_tables.sql
```
