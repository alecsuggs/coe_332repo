# Sample Use Case Diagram of ISS Tracker App

There is a container running a flask application on a remote server. You know the ip address of the server
and the port number that you will be listening on. The diagram below depicts how a user interested in the
ISS tracking data would interface with the flask application to receive information on what countries are
included in the data.


![Use Case Diagram](/homework7/coe332hw7image.png)


The diagram assumes that you have the data files you want to inspect inside the container and the flask application
is currently running inside the container. The first step is to load the json files into the flask python script.
We can do this by entering the command `curl -X POST 127.0.0.1:5032/load` on the command line of a linux terminal.
Now that the data is loaded into the application we can use a few different commands to view certain aspects of the 
data. For this example the user wants to see which countries are included in the data files. The user will enter
`curl 127.0.0.1:5032/countries` and receive a dictionary of all the countries included in the application.

## Source Files

The source files from this containerized flask application can be found on [GitHub](https://github.com/alecsuggs/coe_332repo/tree/main/midterm).


