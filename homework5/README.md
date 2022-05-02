
# Containerized Flask Application with Redis Database


## Description:

This project connects a flask application running in a container with a redis 
database running in a container. The flask application is designed to store meteorite
landing data in the redis database so that it may be accessed later after closing 
the redis container.

## How to Pull the Application Image from Docker Hub:

In a linux terminal with docker package installed run these commands:

`docker login`

`docker pull alecsuggs/app:hw5`

## How to build your own container from scratch:

In a linux terminal with docker package installed navigate to the directory with these
files inside:

1. Dockerfile
2. app.py
3. Meteorite_Landings.json
4. requirements.txt

The first two files should already exist, but we must get the other two files. First 
we will download the Meteorite_Landings.json file by running this command:

`wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json`

Next we must write a requirements text file using your preferred text editor with these lines:

`Flask==2.0.3`

`redis`

Now ensuring you have all 4 of the files in your present working directory we can build
the container. To build your own container run this command:

`docker build -t <username>/<imagename>:1.0`

## Running the Application Container:

If you are using the imaged pulled from docker hub you can start the application container
with this command:

`docker run --name "pick a container name" -p <userport#>:5000 alecsuggs/app:hw5`

If you are using your own image:

`docker run --name "pick a container name" -d -p <userport#>:5000 <username>/<imagename>:1.0`

## How to launch the redis container:

First make sure you have the redis official image:

`docker pull redis:6`

Run this command in your linux terminal:

`docker run -d -p <yourport#>:6379 -v $(pwd)/data:/data:rw --name=<rediscontainername> redis:6 --save 1 1`

This will create a data file in your present working directory that will store the redis database
information even if the container is stopped. This will name the container and run it on your port using
the official redis:6 image. The -d option will detach this from your terminal. 

## How to operate the application to see the meteorite landing data:

First run this command:

`curl -X POST 127.0.0.1:<yourport#>/data`

This loads the data into the redis database. Next run this command to see the meteorite landing 
data in json format.

`curl 127.0.0.1:5032/data`

The data should be output in this format:

```
{
  "meteorite_landings": [
    {
      "GeoLocation": "(-75.6691, 60.6936)",
      "id": "10001",
      "mass (g)": "5754",
      "name": "Gerald",
      "recclass": "H4",
      "reclat": "-75.6691",
      "reclong": "60.6936"
    },
    {
      "GeoLocation": "(-9.4378, 49.5751)",
      "id": "10002",
      "mass (g)": "1701",
      "name": "Dominique",
      "recclass": "L6",
      "reclat": "-9.4378",
      "reclong": "49.5751"
    },
```

This is a standard json output format.