from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

def parse_results(results):
    parsed_results = []
    idx = 0

    for idx, item in enumerate(results):

        item_dict = dict(item)
        parsed_results.append(item_dict)

    print('%9i Results found' %  idx)

    parsed_results = pd.DataFrame(parsed_results)

    return parsed_results

def parse_vehicle_urls(results):
    print('Parsing the ads')

    url_list = results['url']

    vehicle_list = []

    for k, url in enumerate(url_list):
        vehicle = dict()

        rsp = requests.get(url)

        html = bs4(rsp.text, 'html.parser')
        vehresults = html.body.find_all('p', attrs={'class':'attrgroup'})

        try:
            vyear = vehresults[0].find_all('span')[0].get_text()[0:4]
            vehicle['Year'] = vyear
            vehicle_info = vehresults[1].find_all('span')

            for l in range(len(vehicle_info)):
                attribute, value = vehicle_info[l].get_text().split(':')
                vehicle[attribute] = value

            vehicle_list.append(vehicle)

        except IndexError:
            print('Post %9i was likely deleted'% k)


    return vehicle_list