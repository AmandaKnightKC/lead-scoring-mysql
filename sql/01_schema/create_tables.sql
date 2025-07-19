DROP TABLE IF EXISTS applications;
DROP TABLE IF EXISTS quotes;
DROP TABLE IF EXISTS marketing_leads;
DROP TABLE IF EXISTS agent_quota;
DROP TABLE IF EXISTS agent_data;

CREATE TABLE agent_data (
    agent_id INT PRIMARY KEY,
    agent_name VARCHAR(100),
    agent_ramp VARCHAR(50),
    start_date DATE,
    term_date DATE,
    login_email VARCHAR(100)
);
CREATE TABLE agent_quota (
    start_date DATE,
    end_date DATE,
    product_name VARCHAR(100),
    agent_id INT,
    ramp_month_code VARCHAR(10),
    sales_quota INT
);
CREATE TABLE marketing_leads (
    lead_id INT PRIMARY KEY,
    cost VARCHAR(100),
    lead_source VARCHAR(50),
    lead_creation_date DATETIME,
    contact_timestamp DATETIME,
    agent_id INT
);
CREATE TABLE quotes (
    agent_name VARCHAR(100),
    product_name VARCHAR(100),
    created_date DATE,
    lead_id INT,
    FOREIGN KEY (lead_id) REFERENCES marketing_leads(lead_id)
);

CREATE TABLE applications (
    application_id INT PRIMARY KEY AUTO_INCREMENT,
    agent_id INT,
    product_name VARCHAR(100),
    submitted_timestamp DATETIME,
    lead_id INT,
    FOREIGN KEY (lead_id) REFERENCES marketing_leads(lead_id)
);