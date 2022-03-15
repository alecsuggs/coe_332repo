#!/usr/bin/env python3
import json
from typing import List
import logging
import socket
import sys

format_str=f'[%(asctime)s {socket.gethostname()}] %(filename)s:%(funcName)s:%(lineno)s - %(levelname)s: %(message)s'
logging.basicConfig(level=logging.WARNING, format=format_str)


def compute_average_mass(a_list_of_dicts: List[dict], a_key_string: str) -> float:
    """
    Iterates through a list of dictionaries, pulling out values associated with
    a given key. Returns the average of those values.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value (will enforce float type).

    Returns:
        result (float): Average value.
    """
    if (len(a_list_of_dicts) == 0):
        logging.error('a list of dicts is empty')
    total_mass = 0.
    for item in a_list_of_dicts:
        total_mass += float(item[a_key_string])
    return(total_mass / len(a_list_of_dicts) )


def check_hemisphere(latitude: float, longitude: float) -> str:
    """
    Given latitude and longitude in decimal notation, returns which hemispheres
    those coordinates land in.

    Args:
        latitude (float): Latitude in decimal notation.
        longitude (float): Longitude in decimal notation.

    Returns:
        location (string): Short string listing two hemispheres.
    """
    if latitude == 0 or longitude == 0:
        #logging.error('youre not really in a hemisphere')
        raise(ValueError)
    location = 'Northern' if (latitude > 0) else 'Southern'
    location = f'{location} & Eastern' if (longitude > 0) else f'{location} & Western'
    return(location)


def count_classes(a_list_of_dicts: List[dict], a_key_string: str) -> dict:
    """
    Iterates through a list of dictionaries, and pulls out the value associated
    with a given key. Counts the number of times each value occurs in the list of
    dictionaries and returns the result.

    Args:
        a_list_of_dicts (list): A list of dictionaries, each dict should have the
                                same set of keys.
        a_key_string (string): A key that appears in each dictionary associated
                               with the desired value.

    Returns:
        classes_observed (dict): Dictionary of class counts.

    """
    classes_observed = {}
    for item in a_list_of_dicts:
        if item[a_key_string] in classes_observed:
            classes_observed[item[a_key_string]] += 1
        else:
            classes_observed[item[a_key_string]] = 1
    return(classes_observed)


def main():
    logging.debug('entering main loop')
    with open(sys.argv[1], 'r') as f:
        ml_data = json.load(f)
    ne = 0
    nw = 0
    se = 0
    sw = 0
    totalmeteors = 0
    print()
    print()
    print('Summary Data of Meteorite analysis:')
    print()
    logging.debug(f'the type of ml_data is {type(ml_data)}')

    for r in range(len(ml_data['meteorite_landings'])):
        hemi = check_hemisphere(float(ml_data['meteorite_landings'][r]['reclat']), float(ml_data['meteorite_landings'][r]['reclong']))
        if hemi == "Northern & Eastern":
            ne = ne + 1
        elif hemi == "Northern & Western":
            nw = nw + 1
        elif hemi == "Southern & Eastern":
            se = se + 1
        elif hemi == "Southern & Western":
            sw = sw + 1
    print('There were ', ne, ' meteors found in the North East quadrant')
    print('There were ', nw, ' meteors found in the North West quadrant')
    print('There were ', se, ' meteors found in the South East quadrant')
    print('There were ', sw, ' meteors found in the South West quadrant')
    classdictionary = count_classes(ml_data['meteorite_landings'], 'recclass')
    reclasslist = list(classdictionary)
    print()
    print('Class Summary Data:')
    for row in range(len(reclasslist)):
        print('The', reclasslist[row], 'class was found ', classdictionary[reclasslist[row]], 'times')
        totalmeteors = totalmeteors + classdictionary[reclasslist[row]]
    print()
    print('Average mass of',totalmeteors, 'meteors:')
    print(compute_average_mass(ml_data['meteorite_landings'], 'mass (g)'), 'grams')
    print()
    print()

if __name__ == '__main__':
    main()

