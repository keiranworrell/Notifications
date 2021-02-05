import platform
import os
import requests
import datetime
import time

# Fetch data
def covid_data():
    covidData = None
    try:
        covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/uk")
    except:
        # Data has not been found for some reason
        print("Request failed, please check internet connection")

    if (covidData != None):
        data=covidData.json()['Success']
        return data

# send notification to system
def push(title, message):
    sys = platform.system()
    if (sys=='Darwin'):
    	command = f'''
    	osascript -e 'display notification "{message}" with title "{title}"'
    	'''
    elif (sys=='Linux'):
    	command = f'''
    	notify-send "{title}" "{message}"
    	'''
    else:
    	return	
    os.system(command)

covidjson = covid_data()
title = "UK Covid19 stats on {}".format(datetime.date.today())
msg = "Total cases: {totalCases}\nNew cases today: {newCases}\nDeaths today :{newDeaths}".format(
    totalCases = covidjson['cases'],
    newCases = covidjson['todayCases'],
    newDeaths = covidjson['todayDeaths'])
push(title, msg)
