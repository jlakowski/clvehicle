# clvehicle
looking on craigslist for vehicle listings

name a city, make and model and this script will spit out a .csv with all the relevant info on all the relevant vehicles.

i've had the most success with a virtualenv

start up your virtual env
```
pip install python-craigslist
pip install bs4
pip install pandas
```

Usage:
```
python clvehicles.py [city] [make] [model]
```
