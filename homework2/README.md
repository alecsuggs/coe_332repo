HOMEWORK 2

Description:

This folder contains two python files. One file writes the coordinates of five meteorite landing sites 
to json file. The othe file reads this json file and calculates time data concerned with this Mars rover mission. In this mission a rover must travel to five consecutive meteorite landing sites on the surface of Mars. The rover starts at an original position input into calculatetrip.py and goes in order of the sit ID number. The goal of this project is to calculate the number of legs, time to travel between sites
time to sample, and the total mission time.  

generatesites.py:

This python file creates a single "sites" directory with five directory entries in it. Each of these
five directories includes the ID number, latitude, longitude, and composition of the 5 meteorite landing sites. This directory is writen to a json file named sites.json.

calculatetrip.py:

This python file reads the sites.json file created by generatesites.py. The latitude and longitude from
the sites.json file is used in the Great-circle distance formula to calculate the distance the rover 
travel. The travel distance is divided by the rovers speed of 10 km/hr to find the travel time.
The sum of all the travel times and the sample time is added together to find the total mission time.
The composition of the landing site influences the time the sample will take. There are three types of
compositions: stony, iron, and stony-iron that take 1,2, and 3 hours respectively.

Instructions:

1. Run generatesites.py with python3 command
2. Run calculatetrip.py with puthon3 command
3. output is displayed with leg number, travel time, sample time, and the total elapsed time

