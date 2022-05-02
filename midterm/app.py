#!/usr/bin/env python3

from flask import Flask, jsonify
import xmltodict
import logging
import socket
format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=format_str)

app = Flask(__name__)

global positionaldata
global sightings


@app.route('/load', methods=['POST'])
def data_upload() -> str:
    """
    This function responds to a user POST method and downloads the XML ISS data
    files into the application's memory to be accessed later.

    :return: This function returns a string to the user informing them that the data
    was uploaded successfully
    """
    logging.info('data upload requested')
    global positionaldata
    global sightings
    with open('ISS.OEM_J2K_EPH.xml', 'r') as f:
        positionaldata = xmltodict.parse(f.read())
    with open('XMLsightingData_citiesINT01.xml', 'r') as f:
        sightings = xmltodict.parse(f.read())
    return "data loaded successfully! \n"


@app.route('/help', methods=['GET'])
def help() -> str:
    """
    This function responds to a get curl request and outputs a string
    message with information on how to operate the flask application.

    :return: The function returns a string message through the URL route
    /help with information on how to operate the flask application
    """
    logging.info('Help requested')
    return "\n There are 11 commands to interact with this application \n" \
           "\n *** TO RUN ANY COMMAND YOU MUST LOAD DATA FIRST POST URL/load *** \n \n" \
            "The 11 commands are listed below: \n" \
           "1. curl URL/help --- returns this list again \n" \
           "2. curl -X POST URL/load --- loads the data files into the application \n" \
           "3. curl URL/epochs -- returns a list of all the epochs in the data files \n" \
           "4. curl URL/epochs/<epoch> --- insert desired epoch in <> for all data about the <epoch> \n" \
           "5. curl URL/countries --- returns a list of all the countries in the data files \n" \
           "6. curl URL/countries/<country> --- returns all data about the specified <country> \n" \
           "7. curl URL/countries/<country>/regions --- returns all the regions in the specified <country> \n" \
           "8. curl URL/countries/<country>/regions/<region> --- returns all data for the specified <region> \n" \
           "9. curl URL/countries/<country>/regions/<region>/cities --- returns a list of the cities in the <region>\n" \
           "10. curl URL/countries/<country>/regions/<region>/cities/<cities> --- returns all the data for the <city>\n" \
           "11. curl URL/ --- to get to the welcome page"

@app.route('/', methods=['GET'])
def welcome_page() -> str:
    """
    This function prints a welcome page for the base URL to
    the flask application


    :return: This function outputs a string message to the user giving
    instructions for more help
    """
    logging.info('Traveling to the home page!')
    return "This is Alexander's Flask Application \n" \
           "For information on how to operate the app request URL path /help \n"


@app.route('/epochs', methods=['GET'])
def all_epochs() -> dict:
    """
    This function responds to a curl get request and outputs
    a list of the epochs from the positional data.


    :return: This function  prints a dictionary of all the epochs
    """
    logging.info('all epochs requested')
    epochs = {}
    for i in range(0, len(positionaldata['ndm']['oem']['body']['segment']['data']['stateVector'])):
        epochs.update({i + 1: positionaldata['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH']})

    epochs = jsonify(epochs)
    return epochs


@app.route('/epochs/<epoch>', methods=['GET'])
def epoch_info(epoch) -> dict:
    """
    This function responds to a curl get request to the application
    and displays all the information about a specific epoch.

    :param epoch: This function takes in a specific epoch from the user through the URL

    :return: This function prints a dictionary containing all the information
    tied to a specific epoch
    """
    logging.info('epoch information requested')
    for i in range(len(positionaldata['ndm']['oem']['body']['segment']['data']['stateVector'])):
        if positionaldata['ndm']['oem']['body']['segment']['data']['stateVector'][i]['EPOCH'] == str(epoch):
            info = jsonify(positionaldata['ndm']['oem']['body']['segment']['data']['stateVector'][i])
            return info


@app.route('/countries', methods=['GET'])
def countries() -> dict:
    """
    This function responds to a curl get request to the application and
    returns a list of all the countries included in the sightings data

    :return: This function returns a dictionary of all the countries in the sightings datafile

    """
    logging.info('all countries requested')
    allcountries = {}
    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['country'] not in allcountries:
            allcountries.update({sightings['visible_passes']['visible_pass'][i]['country']: i+1})
    allcountries = jsonify(allcountries)
    return allcountries


@app.route('/countries/<country>', methods=['GET'])
def country_info(country) -> dict:
    """
    This function takes in a country name by the user through the URL with
    a curl get request and outputs data associated to with the country.

    :param country: The user specifies the country in the URL

    :return: The function returns a dictionary holding information on the sighting data for the
    specified country
    """
    logging.info('country information requested')
    countryinfo = {}
    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['country'] == str(country):
            countryinfo.update({i + 1: sightings['visible_passes']['visible_pass'][i]})
    countryinfo = jsonify(countryinfo)
    return countryinfo


@app.route('/countries/<country>/regions', methods=['GET'])
def regions(country) -> dict:
    """
    This function takes in a country name from the user through the URL
    with a curl get request and outputs a list of regions inside the specified country

    :param country: The user specifies the country by inputing it into the URL
    :return: The function returns a printed list of
    """
    logging.info('regions in a country requested')
    allregions = {}
    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['country'] == str(country):
            if sightings['visible_passes']['visible_pass'][i]['region'] not in allregions:
                allregions.update({sightings['visible_passes']['visible_pass'][i]['region']: i+1})
    allregions = jsonify(allregions)
    return allregions


@app.route('/countries/<country>/regions/<region>', methods=['GET'])
def region_info(country, region) -> dict:
    """
    This function prints information about a specified region. The user inputs
    the parameters country and region through the URL and a curl get request

    :param country: This is the country in which the specified region is located
    :param region: This is the name of the region the user wants more information about

    :return: The function returns a dictionary of all the information associated
    with the region and country the user specified.
    """
    logging.info('information about a region requested')
    regioninfo = {}
    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['country'] == str(country):
            if sightings['visible_passes']['visible_pass'][i]['region'] == str(region):
                regioninfo.update({i+1: sightings['visible_passes']['visible_pass'][i]})
    regioninfo = jsonify(regioninfo)
    return regioninfo


@app.route('/countries/<country>/regions/<region>/cities', methods=['GET'])
def cities(country, region) -> dict:
    """
    This function inputs a country and region from the user in the URL
    using a curl get request and outputs a printed list of all the countries
    in the specified country and region.

    :param country: The user inputs the country for which they want
    to see the cities listed
    :param region: The user inputs the region for which they want to see
    all the cities listed
    :return: The function returns a dictionary of all the cities in the
    specified country and region.
    """
    logging.info('cities in a region requested')
    allcities = {}

    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['country'] == str(country):
            if sightings['visible_passes']['visible_pass'][i]['region'] == str(region):
                if sightings['visible_passes']['visible_pass'][i]['city'] not in allcities:
                    allcities.update({sightings['visible_passes']['visible_pass'][i]['city']: i+1})
    allcities = jsonify(allcities)
    return allcities


@app.route('/countries/<country>/regions/<region>/cities/<city>', methods=['GET'])
def city_info(country, region, city) -> dict:
    """
    this function takes a city parameter in from the user in the URL of a curl get
    request and outputs all the data about the specified city.

    :param city: The city that the user wants to see all the data about
    :param country: The country where the desired city exists
    :param region: The region where the desired city exists
    :return: The function returns a dictionary of all the information about the specified city
    """
    cityinfo = {}
    logging.info('city information requested')
    for i in range(0, len(sightings['visible_passes']['visible_pass'])):
        if sightings['visible_passes']['visible_pass'][i]['city'] == str(city):
            if sightings['visible_passes']['visible_pass'][i]['country'] == str(country):
                if sightings['visible_passes']['visible_pass'][i]['region'] == str(region):
                    cityinfo.update({i+1: sightings['visible_passes']['visible_pass'][i]})
    cityinfo = jsonify(cityinfo)
    return cityinfo

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
