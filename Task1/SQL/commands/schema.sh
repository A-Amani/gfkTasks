#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE TABLE dataset_B (
	   productid INTEGER, 
	   brand TEXT, 
	   RAM_GB INTEGER,
	   HDD_GB INTEGER,
	   GHz	DECIMAL,
	   price INTEGER
	);
EOSQL
