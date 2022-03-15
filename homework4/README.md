Homework #4

Description:
This project contains data, in JSON format, from meteorite
samples taken from the surface of Mars. This data is input
into the ml_data_analysis.py file where it is compiled and
a summary of the data is output. Inside the project there
is a test_ version of the ml_data_analysis file used for 
unit testing the functions in the main file. The project
contains a dockerfile that containerizes all the necessary
files for the homework 4 project.

ml_data_analysis.py-
This file contains three functions and a main() function.
One function checks the hemisphere of the coordinates of
the landing site. One function computes the average mass
of all the meteor samples recovered. The last function
counts all the classes in all the sample data and returns
a dictionary with all the classes and their respective 
tally count. The main function uses these three functions
to output a detailed summary of the meteor data analysis.

test_ml_data_analysis.py-
This file contains 3 test functions for each of the functions
in the ml_data_analysis.py file. Each test function contains 
five tests. These tests measure expected values, return types,
and return errors.

Meteorite_Landings.json-
This file contains the meteorite sample data in a list of
dictionaries named "meteorite_landings". Each item in the list
has seven entries in it.

Dockerfile-
This file contains the steps to create the Docker image.

Instructions:

To Pull and Use Image from Docker Hub Inside Linux Interface-
1. type "docker pull ml_data_analysis" on command line
2. type "docker run ml_data_analysis" on command line

To Build an Image from Dockerfile in Linux Interface-
1. navigate until the Dockerfile is in the current working directory
2. type "docker build *yourfilenamehere*"

To Run the code in a container with given data-
1. type "docker run --rm -it -v $PWD:/data alecsuggs/ml_data_analysis:hw04 /bin/bash"
in command line
2. type "cd /data" on command line
3. type "ml_data_analysis.py Meteorite_Landings.json" on command line

To Run the code with user provided data-
1. Insert the json file with data in the directory with other files 
2. type "docker run --rm -it -v $PWD:/data alecsuggs/ml_data_analysis:hw04 /bin/bash"
in command line
3. type "cd /data" on command line
4. type "ml_data_analysis.py *nameofyourfile*.json" on command line

To run pytest in container-
1. type "docker run --rm -it -v $PWD:/data alecsuggs/ml_data_analysis:hw04 /bin/bash"
in command line
2. type "cd /data" on command line
3. type "pytest" on command line

Input Data Requirements:

{
  "meteorite_landings" : [
    {
      "name": "Ruiz",
      "id": "10001",
      "recclass": "L5",
      "mass (g)": "21",
      "reclat": "50.775",
      "reclong": "6.08333",
      "GeoLocation": "(50.775, 6.08333)"
    },

The json file should contain one list of dictionaries
with every landing site's data. Each landing site 
should have seven data points like the sample above.

The output data should include a summary of the hemispheres
the meteors were found in, a summary of the classes of meteor
found, and the average mass of the meteor samples in
grams.

Link for Additional Data:
https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json

Download this json file to the directory containing the files
before running