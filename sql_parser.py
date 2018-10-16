import pandas as pd
import re
import numpy as np
from functions import split_select, column_name, split_from, table_name, inner_join_table_split, inner_join_table


df_sql = pd.read_csv('sample_queries.csv')
df_sql = df_sql.rename(columns={'QUERY_ID': 'Query_ID'})

#columns parsing
df_sql['QUERY_TEXT'] = df_sql['QUERY_TEXT'].str.lower()
# Calling on the split_select which splits the QUERY_TEXT to grab text anything between ("select" to "from")
df_sql['Columns'] = df_sql['QUERY_TEXT'].apply(lambda year2: split_select(year2))
# Any column that has a "*" will be replaced with "all columns"
df_sql['Columns'] = df_sql['Columns'].str.replace('*', 'all_columns')
# Calling on the column_name function which parses the columns after the select statement
df_sql['Columns'] = df_sql['Columns'].apply(lambda cols2: column_name(cols2))

# tables Parsing
# Calling on the split_from which splits the QUERY_TEXT to grab text anything between ("from" to either "join", "where", or any new line)
df_sql['Tables'] = df_sql['QUERY_TEXT'].apply(lambda from2: split_from(from2))
# Calling on the table_name function which parses the tables after the from statement
df_sql['Tables'] = df_sql['Tables'].apply(lambda tabs: table_name(tabs))

# # Inner join Tables
# # Calling on the inner_join_table_split which splits the QUERY_TEXT to grab text anything between ("select" to "from")
# df_sql['Inner Join'] = df_sql['QUERY_TEXT'].apply(lambda split1: inner_join_table_split(split1))
# # Replacing for error purposes
# df_sql['Inner Join Table #2'] = df_sql['Inner Join'].replace(np.NaN, 'no inner')
# # Calling on the inner_join_table function which parses the tables after the inner join statement
# df_sql['Inner Join Table #2'] = df_sql['Inner Join Table #2'].apply(lambda split2: inner_join_table(split2))


df_sql.to_csv('parsed.csv', index=False)
