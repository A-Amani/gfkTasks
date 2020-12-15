#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	copy (
	    SELECT brand, RANK() OVER(PARTITION BY brand ORDER BY price ASC) 
 	    FROM dataset_B 
	)
	TO '/var/lib/postgresql/dump/2a-rank.csv'  CSV HEADER;
EOSQL
