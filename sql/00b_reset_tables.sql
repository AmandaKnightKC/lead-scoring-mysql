USE lead_scoring;
SET FOREIGN_KEY_CHECKS = 0;
-- Disable foreign key checks to allow truncating tables with dependencies.
TRUNCATE TABLE agent_data;
TRUNCATE TABLE agent_quota;
TRUNCATE TABLE applications;
TRUNCATE TABLE leads;
TRUNCATE TABLE marketing_leads;
TRUNCATE TABLE quotes;
SET FOREIGN_KEY_CHECKS = 1;
-- Re-enable foreign key checks after truncating the tables.
-- NEXT STEPS:
-- 1. run Python script to load data back into the tables
-- 2. run sql/02_explore_leads.sql to explore the data in the tables.