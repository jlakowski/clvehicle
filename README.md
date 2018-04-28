# clvehicle
looking on craigslist for vehicle listings

name a city, make and model and this script will spit out a .csv with all the relevant info on all the relevant vehicles.

i've had the most success with a virtualenv
The best instructions for creating a virtualenv: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/


start up your virtual env
```
pip install python-craigslist
pip install bs4
pip install pandas
pip install sqlalchemy
pip install pymysql
```

Usage:
```
python clvehicles.py [city] [make] [model]

testing commit from pycharm
changed again
```

ConfigurationFiles:
'''
Create a file named MySqlConfigurationString.txt at the same level as clvehicles.py.

The contents of the file should be similar to: mysql+pymysql://root:<<Password>>@localhost/craigslist
'''

MySQL configuartion:
'''
Create the schema craigslist in MySQL by running the file: CreateSchema_craigslists.sql
'''
