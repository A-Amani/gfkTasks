#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
	COPY dataset_B(
		   productid,
		   brand,
		   RAM_GB,
		   HDD_GB,
		   GHz,
		   price)

	FROM '/var/lib/postgresql/mytsv/dataset_B.tsv'
	DELIMITER '	'
	CSV HEADER;
EOSQL
