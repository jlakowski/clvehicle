from craigslist import CraigslistForSale
import csv
import sys
import pandas as pd
import parse_craigslist

def main(argv):
    if len(argv) < 4:
        print('please enter $python clvehicles.py [city] [make] [model]')
        sys.exit()

    location = argv[1]
    make = argv[2]
    model = argv[3]

    fileName = '' + location + '_' + make + '_' + model + ''
    folder = '../FileDump/'

    print('Searching the ' + location + ' craigslist site for ' + make + ' ' + model)
    cl_s = CraigslistForSale(site=location, filters={'make': make, 'model': model, 'min_price': 2000})


    results = cl_s.get_results()
    results_df = parse_craigslist.parse_results(results)
    list_of_dics = parse_craigslist.parse_vehicle_urls(results_df)


    vehicles_df = pd.DataFrame(list_of_dics)
    vehicles_df.index.name = 'VehicleKey'


    vehicles_df.to_csv(folder + fileName, sep='|')



if __name__ == "__main__":
    main(sys.argv)
