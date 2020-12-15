#!/bin/bash

mongoimport --type csv -d mydb -c 2a-rank --headerline data/mycsv/2a-rank.csv
mongoimport --type csv -d mydb -c 2b-minMax --headerline data/mycsv/2b-minMax.csv
mongoimport --type csv -d mydb -c 2c-medianQuery --headerline data/mycsv/2c-medianQuery.csv

