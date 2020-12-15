import os
from pyspark.sql import SparkSession


def merge(df1, df2, join_type, join_key: str, path):
    assert join_type in ["inner", "outer", "left", "right", "left_semi", "left_anti"]
    res_df= df1.join(df2, on=join_key, how=join_type)
    res_df.coalesce(1).write.csv(f'{path}/merge_{join_type}.csv', header='true')


if __name__ == "__main__":
    spark = SparkSession.builder.appName('gfk-task1').getOrCreate()
    wd = os.path.join(os.environ['HOME'], "res")

    df1 = spark.read.csv(f'{wd}/task2_df1.csv', header=True)
    df2 = spark.read.csv(f'{wd}/task2_df2.csv', header=True)

    merge_types = ["inner", "outer"]

    for merge_type in merge_types:
        merge(df1, df2, join_type=merge_type, join_key="id", path=wd)


