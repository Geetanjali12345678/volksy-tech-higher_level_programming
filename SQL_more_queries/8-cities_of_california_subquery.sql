-- create table
SELECT id,name FROM cities WHERE state_id in (SELECT id FROM STATES WHERE name = 'California') ORDER BY id ASC;
