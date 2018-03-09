from craigslist import CraigslistForSale
import csv
from bs4 import BeautifulSoup as bs4
import requests
from vehicle import Vehicle
import sys
#Jim wrote this on November 16, 2017
#i wrote the vehicle class for this too

#TODO:
#find a way to handle the unicode charater error...

# DONE and command line args for city make and model
# create a column for rounding the milage to the nearest 5k
#also find a way to check if 150 miles means 150 or 150,000
#and modularize this script to turn it into a proper program


def main(argv):
    
    if len(argv) < 4:
        print('please enter $python clvehicles.py [city] [make] [model]')
        sys.exit()
    
    location = argv[1]
    make = argv[2]
    model = argv[3]

    print('Searching the ' + location + ' craigslist site for ' + make + ' ' + model)
    cl_s = CraigslistForSale(site=location, filters={'make':make, 'model':model,'min_price':2000})
    i = 0
    urls = []
    nresults = sum(1 for x in cl_s.get_results())

    vehicles = []

    for result in cl_s.get_results():
        #print result
        urls.append(result['url'])
        veh = Vehicle(result['name'])
        veh.setPrice(result['price'])
        veh.setTimestamp(result['datetime'])
        veh.setURL(result['url'])
        veh.setID(result['id'])
        vehicles.append(veh)

        i = i +1 
    print i

    print('Parsing the ads')
    for k in range(len(vehicles)):
        rsp = requests.get(urls[k])

        html = bs4(rsp.text, 'html.parser')
        vehresults = html.body.find_all('p', attrs={'class':'attrgroup'})
        #find a way of turning this into a dictionary
        try:
            vyear = vehresults[0].find_all('span')[0].get_text()[0:4]
            vehicles[k].setYear(vyear)
            vehicle_info = vehresults[1].find_all('span')
            for l in range(len(vehicle_info)):
                attribute = vehicle_info[l].get_text().split(':')
                if attribute[0] == 'condition':
                    vehicles[k].setCondition(attribute[1])
                elif attribute[0] == 'cylinders':
                    vehicles[k].setCylinders(attribute[1])
                elif attribute[0] == 'drive':
                    vehicles[k].setDrive(attribute[1])
                elif attribute[0] == 'fuel':
                    vehicles[k].setFuel(attribute[1])
                elif attribute[0] == 'odometer':
                    vehicles[k].setMilage(attribute[1])
                elif attribute[0] == 'paint color':
                    vehicles[k].setColor(attribute[1])
                elif attribute[0] == 'title status':
                    vehicles[k].setTitleStatus(attribute[1])
                elif attribute[0] == 'transmission':
                    vehicles[k].setTranstype(attribute[1])
                elif attribute[0] == 'type':
                    vehicles[k].setVehicletype(attribute[1])


        except IndexError:
            print('Post %d was likely deleted', k)

    headers = ['name', 'price','year', 'condition', 'milage', 'title status', 'transmission', 'drive','cylinders', 'fuel', 'color','location', 'timestamp', 'url']

    print('writing to .csv')
    fname = location + model + '.csv'
    with open(fname,'wb') as f:
        w = csv.writer(f)
        i = 0
        w.writerow(headers)

        for i in range(len(vehicles)):
            try:
                name = vehicles[i].name

            except AttributeError:
                name = 'N/A'
            try:
                price = vehicles[i].price

            except AttributeError:
                price = 'N/A'

            try:
                condition = vehicles[i].condition
            except AttributeError:
                condition = 'N/A'

            try:
                milage = vehicles[i].milage
            except AttributeError:
                milage = 'N/A'

            try:
                titleStatus = vehicles[i].titleStatus
            except AttributeError:
                titleStatus = 'N/A'

            try:
                transtype = vehicles[i].transtype
            except AttributeError:
                transtype = 'N/A'

            try:
                drive = vehicles[i].drive
            except AttributeError:
                drive = 'N/A'

            try:
                cylinders = vehicles[i].cylinders
            except AttributeError:
                cylinders = 'N/A'

            try:
                fuel= vehicles[i].fuel
            except AttributeError:
                fuel= 'N/A'

            try:
                color = vehicles[i].color
            except AttributeError:
                color = 'N/A'

            try:
                timestamp = vehicles[i].timestamp
            except AttributeError:
                timestamp = 'N/A'

            try:
                url = vehicles[i].url
            except AttributeError:
                url = 'N/A'

            try:
                year = vehicles[i].year
            except AttributeError:
                year = 'N/A'

            row = [name, price, year, condition, milage, titleStatus, transtype, drive, cylinders, fuel, color,location, timestamp, url]
            try:
                w.writerow(row)
            except UnicodeEncodeError:
                print("weird character")

if __name__ == "__main__":
    main(sys.argv)

class Vehicle:
    
    def __init__(self, tag):
        self.name = tag
    
    def setTag(self, tag):
        self.tag = tag

    def setPrice(self, price):
        self.price = price

    def setURL(self, url):
        self.url = url

    def setCondition(self, cond):
        self.condition = cond
    
    def setCylinders(self, ncyl):
        self.cylinders = ncyl
    
    def setDrive(self, drive):
        self.drive = drive

    def setFuel(self, fuel):
        self.fuel = fuel
        
    def setMilage(self, odometer):
        self.milage = odometer
    
    def setColor(self, color):
        self.color = color
    
    def setTitleStatus(self, titleStat):
        self.titleStatus = titleStat
        
    def setTranstype(self, transtype):
        self.transtype = transtype

    def setVehicletype(self, vehicletype):
        self.vehicletype = vehicletype
    
    def setTimestamp(self, tstamp):
        self.timestamp = tstamp
    
    def setID(self, idn):
        self.idn = idn
    
    def setYear(self, year):
        self.year = year
