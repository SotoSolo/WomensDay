import numpy as np
import pandas as pd
import psycopg2 as pg
import pandas.io.sql as psql
from configparser import ConfigParser
import time

# View the all columns of a data frame at the console
pd.set_option('display.width', None)
pd.set_option('display.max_columns', None)

# Read the config file
config_object = ConfigParser()
config_object.read("db_config.ini")

# GreenPlum schema
gplum = config_object['GREENPLUM']

# %% Establish db connection
user = gplum['user']
password = gplum['password']
host = gplum['host']
dbname = gplum['dbname']
port = gplum['port']

# Start time
start_query = time.time()

with pg.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port, dbname, user, password),
                options='-c statement_timeout=0') as conn:
    df1 = psql.read_sql(f''' 
        
                ''', conn)
end_query = time.time()

total = np.round((end_query - start_query), 3)

print('\n Total Query execution: ' + str(total) + ' seconds')