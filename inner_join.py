import pandas as pd
import re
import numpy as np

#prints all of the join staetements of query
def inner_join_table(innerjoin):
    x = re.findall(r'join\s(.*)\n', innerjoin)
    if x:
        return(x)
# Prints all the where statements of query
def where_table(where):
    x = re.findall(r'where\s(.*)\w+', where)
    if x:
        return(x)


df_sql = pd.read_csv('sample_queries.csv')
# df_sql['Inner Join Columns2'] = df_sql['QUERY_TEXT'].apply(lambda innerjoin: inner_join_table(innerjoin))
source = []
for x in df_sql['QUERY_TEXT'].apply(lambda innerjoin: inner_join_table(innerjoin)):
    source.append(x)
print(source)

source2 = []
for x in df_sql['QUERY_TEXT'].apply(lambda where: where_table(where)):
    source2.append(x)
print(source2)
