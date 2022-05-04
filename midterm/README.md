
# International Space Station Tracker Application

This project consists of 5 files total. This project provides an application designed
to allow a user to search for data in the ISS sightings and positions XML files from NASA.
The XML files contain a large amount of data, so it is hard to search for specific data. This
application allows a user to search for specific data and see it returned in an easy-to-read 
format.

## Obtaining data of ISS positions and sightings

The data used by the tracker application can be downloaded from the following links in a web browser:
1. [Position Data] (https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml)
2. [Sightings Data] (https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT01.xml)
***Do not change the name of the data files when saving***

To download in Linux terminal:

`wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_OEM/ISS.OEM_J2K_EPH.xml`

`wget https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-13/ISS_sightings/XMLsightingData_citiesINT01.xml`

## Instructions to build a container from Dockerfile

First the user must create a text file named `requirements.txt` with these three lines in it:
```
Flask==2.0.3
pytest==7.0.0
xmltodict
```

Next check files that should be in the current directory:
1. Dockerfile
2. Makefile
3. ISS.OEM_J2K_EPH.xml
4. XMLsightingData_citiesINT01.xml
5. app.py
6. requirements.txt

After confirming that all these files are in the current directory run these commands in the linux terminal:

`docker build -t <username>/app:1.0 .`

`docker run --name "ISStrackerapp" -p <yourport#>:5000 <username>/app:1.0`

The docker container should be running at this point. If you do not want to build your own container
a working image can be downloaded from docker hub with these commands in the linux terminal:

`docker login`

`make pull`

`make run`

To run on a port other than 5033:

`docker run --name "ISStrackerapp" -p <portnumber>:5000 alecsuggs/app:1.0`

## Instructions to interact with the application:

Upon starting the application in the container the URL of the application
will be displayed like this:

```
WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://127.0.0.1:5000
 * Running on http://172.17.0.3:5000 (Press CTRL+C to quit)
```

There are a total of 11 commands that the application will respond to.
The 11 commands are listed below:

1. curl URL/help --- returns this list again
2. curl -X POST URL/load --- loads the data files into the application 
3. curl URL/epochs -- returns a list of all the epochs in the data files
4. curl URL/epochs/<epoch> --- insert desired epoch in <> for all data about the <epoch>
5. curl URL/countries --- returns a list of all the countries in the data files
6. curl URL/countries/<country> --- returns all data about the specified <country>
7. curl URL/countries/<country>/regions --- returns all the regions in the specified <country>
8. curl URL/countries/<country>/regions/<region> --- returns all data for the specified <region>
9. curl URL/countries/<country>/regions/<region>/cities --- returns a list of the cities in the <region>
10. curl URL/countries/<country>/regions/<region>/cities/<cities> --- returns all the data for the <city>
11. curl URL/ --- to get to the welcome page

***Command number 2 must be run before any of the other commands***

## Interpreting Outputs:

The outputs of this application are either messages or dictionaries. The messages are
only for the help command, welcome page, and data upload alerts. All the data requested
from the application with regard to the ISS tracking are in the dictionary
format. Below is a sample request and response example:

User input:

`curl -X POST 127.0.0.1:5032/load`

Application Output:

`data loaded successfully!`

Another example....

User Input:

`curl 127.0.0.1:5032/countries/Australia/regions/Victoria/cities`

Application Output:

```
{
  "Ballarat": 956,
  "Benalla": 976,
  "Bendigo": 993,
  "Cobram": 1010,
  "Dandenong": 1026,
  "Melbourne": 1046,
  "Mildura": 1066,
  "Pakenham": 1077,
  "Sale": 1097,
  "Shepparton": 1119,
  "Sunbury": 1136,
  "Traralgon": 1156,
  "Tylden": 1178,
  "Warrnambool": 1188,
  "Yarram": 1210
}
```

## Data Citations:

Position Data-
Goodwin, S. (n.d.). ISS_COORDS_2022-02-13. NASA. https://nasa-
publicdata.s3.amazonaws.com/iss-coords/2022-02-
13/ISS_OEM/ISS.OEM_J2K_EPH.xml  
Retrieved April 15, 2022, from https://data.nasa.gov/Space- 
Science/ISS_COORDS_2022-02-13/r6u8-bhhq

Sightings Data-
Goodwin, S. (n.d.). XMLsightingData_citiesINT01 NASA. Retrieved March 29, 
2022, from https://nasa-public-data.s3.amazonaws.com/iss-coords/2022-02-
13/ISS_sightings/XMLsightingData_citiesINT01.xml