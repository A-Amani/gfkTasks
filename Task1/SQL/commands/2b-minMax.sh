#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	copy (
	    SELECT MIN(HDD_GB), MAX(HDD_GB)
	    FROM dataset_B
	)
	TO '/var/lib/postgresql/dump/2b-minMax.csv'  CSV HEADER;
EOSQL
