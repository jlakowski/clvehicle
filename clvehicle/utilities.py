import time
from sqlalchemy import create_engine
import pymysql

def get_parameters():
    all_sites, write_to = '', ''

    make = input("Enter the make of the vehicle to search: ")
    model = input("Enter the model to search: ")
    all_sites = input("Enter the location to search. Leave blank to crawl all locations. :")
    while write_to not in ['db', 'csv']:
        write_to = input("Write the results to a database or CSVs [db, csv] :")

    return make, model, all_sites, write_to


def result_size_wait(results_size):
    seconds = results_size / 2.0
    print("waiting %5i seconds" % seconds)
    time.sleep(seconds)


def write_df_to_db(vehicles_df, make, model):
    with open('MySQLConnectionString.txt', 'r') as file:
        connection_string = file.readline()

    engine = create_engine(connection_string)
    connection = engine.connect()
    table_name = make + '_' + model

    vehicles_df['id'] = vehicles_df['id'].astype(int)
    vehicles_df = vehicles_df.set_index('id')

    vehicles_df.to_sql(name=table_name, con=connection, if_exists='append', schema='craigslist', index=True)


 

