# Analyzing Turbidity of Mars Lab Water

## Description:
 
This project determines if the water in the Mars Laboratory is safe to
use to analyze the meteorite samples. Inside this folder there is a 
python file analyzewater.py and a test_ file accompaniment.

## IMPORTANT INSTRUCTIONS:
The data on the water quality comes in the json format. This data is
mandatory for the analysis of the water turbidity and must be in the 
same directory as analyzewater.py.

## JSON data package dowload link:

https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

After the JSON data has been downloaded to the current directory
the analyzewater.py file can be executed using Python3. The three
functions in the analyzewater.py file can be unit tested automatically
using the pytest executable. 

The output results of the analyzewater.py file return the safety
status of the Mars laboratory in a message similar to this:

```
Average turbidity based on five most recent measurements 1.1556058
minimum time required to return below threshold =  7.19999999999999  hours
WARNING:root: Turbidity is above threshold for safe use
```

The average turbidity based on the past 5 measurements, minimum time to
reach safety, and a logging warning are output.

### analyzewater.py:

This python script reads in a JSON file containing the turbidity data
for the water. This turbidity data is averaged over the 5 most recent 
measurements and compared to a threshold value for turbidity by a function. 
If the turbidity is too high then a function runs to calculate the amount
of time in hours it will take to reach safe levels.

### test_analyzewater.py:

This script contains 5 tests for each of the three functions in the
file analyzewater.py. This script is executable using pytest to
automate results.

