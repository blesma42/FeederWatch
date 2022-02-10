#This file will read all .csv in a specific folder and pass them to a database.
#Because of the large file size, they are processed chunk-wise
#Because this may take some time it will print out the progress
#After all files are processed it'll also return the number of rows per file and number of chunks as control 

import pandas as pd
import json
from sqlalchemy import create_engine
import os


#get credentials for MySQL/dbms
with open(r'C:\Users\mathi\Desktop\Datenanalyse\Credentials\mysql.json') as json_file:
    db_credentials = json.load(json_file)

#credentials as variables
host='localhost'
user=db_credentials['user']
password=db_credentials['password']
database='feederwatch'
path_to_data=r'C:\Users\mathi\Desktop\Datenanalyse\2022-02-04_FeederWatch\Data'

#etablish connection to the dbms
engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}')
#create new db
engine.execute(f'CREATE DATABASE IF NOT EXISTS {database}')

engine=create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

#dictonary to store files name and number of rows
files_for_db={}

#gets file names and number of rows
for file in os.listdir(path_to_data):
    if file.endswith(".csv"):
        with open(f'{path_to_data}/{file}') as f:
            nrow=sum(1 for line in f)

        files_for_db[file]=[nrow]
        print(f'{file}: {nrow} rows')

def feed_file_to_db(file):
    current_file=file.lower()[:-4]
    chunk_size=1000
    chunk_no=0 #chunk-counter
    expected_chunks=int((files_for_db[file][0]-1)/chunk_size+1) #number of expected chunks
    print(f'starting with {file}')
    #reads and passes file in chunks to db
    for chunk in pd.read_csv(f'{path_to_data}/{file}', chunksize=chunk_size):
        chunk.to_sql(current_file, engine, if_exists='append', method='multi')
        chunk_no+=1
        if chunk_no%10==0:
            print(f'Chunks done: {chunk_no}/{expected_chunks}')
    print('All chunks inserted')
    files_for_db[file].append(chunk_no) #stores number of chunks for later control

for file in files_for_db:
    feed_file_to_db(file)

#control if number of rows and number of chunks fit together
for file in files_for_db:
    print(f'{file}: {files_for_db[file]}')

