#!/bin/bash


/usr/local/spark/bin/spark-submit task2/step1_create_df.py
echo "step1 finished"
/usr/local/spark/bin/spark-submit task2/step2_merge.py
echo "step2 finished"
