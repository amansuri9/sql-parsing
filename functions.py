import re

# Splits the QUERY_TEXT to grab text anything between ("select" to "from")
def split_select(year):
    # Splitting quote text so it can only parse from "select " for columns
    x = re.search('select\s(.*)\sfrom', year)
    if x:
        return(x.group())


# Parses the columns after the select statement
def column_name(select):
    # Parsing columns after select. Can use \S insead of \w
    # Using positive lookbehind to search for word after select
    x = re.search('(?<=select )\w+', select)
    if x:
        return(x.group())
    # Parsing alias columns as " "
    # Using lookahead to search before "as" to match alias column_name
    # example: "table"."level_8" as "level8" it parses "level_8"
    x = re.search('\w+(?=" as)', select)
    if x:
        return(x.group())
    # Parsing alias columns as " "
    x = re.search('(?<=, )\w+', select)
    if x:
        return(x.group())

# Splits the QUERY_TEXT to grab text anything between ("from" to "join", "where" or the end of the line)
def split_from(fromparse):
    # Splitting quote text so it can only parse from "from " for columns for alias
    # that have an return line thats why \n
    x = re.search('from\s(.*)\n', fromparse)
    if x:
        return(x.group())
    x = re.search('from\s(.*)\sjoin', fromparse)
    if x:
        return(x.group())
    x = re.search('from\s(.*)\swhere', fromparse)
    if x:
        return(x.group())
    x = re.search('from\s(.*)', fromparse)
    if x:
        return(x.group())


# parses the tables after the from statement
def table_name(fromparse2):
    # Parsing alias table as "."tablename"
    x = re.search(r'(?<=".")\w+', fromparse2)
    if x:
        return(x.group())
    # Parsing tables after from or use \S insead of \w
    # from "columnname"
    x = re.search('(?<=from )\S+', fromparse2)
    if x:
        return(x.group())


# Splits the QUERY_TEXT to grab text anything between ("join" to another "join" or "where" or the end of the line)
def inner_join_table_split(innerjoin):
    x = re.search('join\s(.*)\n', innerjoin)
    if x:
        return(x.group())
    x = re.search('join\s(.*)\swhere', innerjoin)
    if x:
        return(x.group())
    x = re.search('join\s(.*)\souter join', innerjoin)
    if x:
        return(x.group())
    x = re.search('join\s(.*)\sinner join', innerjoin)
    if x:
        return(x.group())
    x = re.search('join\s(.*)', innerjoin)
    if x:
        return(x.group())

# parses the tables after the from statement for inner join statements
def inner_join_table(innerjoin2):
    x = re.search(r'(?<=".")\w+', innerjoin2)
    if x:
        return(x.group())
    x = re.search(r'(?<=join )\w+',innerjoin2)
    if x:
        return(x.group())
