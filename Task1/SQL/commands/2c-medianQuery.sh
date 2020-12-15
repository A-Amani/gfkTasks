#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	copy (
		SELECT RAM_GB, PERCENTILE_CONT(0.5) WITHIN GROUP(ORDER BY GHz) 
		FROM dataset_B
		GROUP BY RAM_GB
	)
	TO '/var/lib/postgresql/dump/2c-medianQuery.csv'  CSV HEADER;
EOSQL
