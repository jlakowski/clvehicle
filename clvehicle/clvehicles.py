from craigslist import CraigslistForSale
import csv
import sys
import pandas as pd
import parse_craigslist
import os
import utilities
import random
import time

def main():

    make, model, single_site, write_to = utilities.get_parameters()

    if not single_site:
        sites_to_crawl = parse_craigslist.parse_craigslist_sites()
    else:
        sites_to_crawl = [single_site]

    for location in sites_to_crawl:
        file_name = '' + location + '_' + make + '_' + model + ''
        folder = '../FileDump/'

        print('Searching the ' + location + ' craigslist site for ' + make + ' ' + model)
        cl_s = CraigslistForSale(site=location, filters={'make': make, 'model': model, 'min_price': 2000})

        results = cl_s.get_results()
        results_df = parse_craigslist.parse_results(results)
        list_of_dics = parse_craigslist.parse_vehicle_urls(results_df)

        vehicles_df = pd.DataFrame(list_of_dics)
        vehicles_df.index.name = 'VehicleKey'


        if write_to == 'csv':
            if not os.path.exists("../FileDump"):
                os.makedirs("../FileDump")
            vehicles_df.to_csv(folder + file_name, sep='|')
        elif write_to == 'db':
            utilities.write_df_to_db(vehicles_df, make, model)


def new_main():

    make, model, single_site, write_to = utilities.get_parameters()
    sites_to_crawl = []

    while True:

        # uses single site if supplied or request a list of sites to crawl if it is empty
        if not single_site and not sites_to_crawl:
            sites_to_crawl = parse_craigslist.parse_craigslist_sites()
        elif single_site:
            sites_to_crawl = [single_site]

        while sites_to_crawl:
            location = sites_to_crawl.pop(random.randint(0, len(sites_to_crawl)-1))
            file_name = '' + location + '_' + make + '_' + model + ''
            folder = '../FileDump/'


            # get results from craigslist api try again every 6 hours if it fails
            cl_results = ''
            while not cl_results:
                try:
                    print('Searching the ' + location + ' craigslist site for ' + make + ' ' + model)
                    cl_s = CraigslistForSale(site=location, filters={'make': make, 'model': model, 'min_price': 2000})
                    cl_results = cl_s.get_results()
                except:
                    print('Failed to call tha api for the ' + location + ' craigslist site for ' + make + ' ' + model)
                    print("Waiting for 6 hours...")
                    time.sleep(21600)

            results_df = parse_craigslist.parse_results(cl_results)
            list_of_dicts = parse_craigslist.parse_vehicle_urls(results_df, location, make, model, write_to)

            if write_to == 'csv':
                vehicles_df = pd.DataFrame(list_of_dicts)
                vehicles_df.index.name = 'VehicleKey'

                if not os.path.exists("../FileDump"):
                    os.makedirs("../FileDump")

                vehicles_df.to_csv(folder + file_name, sep='|')


if __name__ == "__main__":
    new_main()
