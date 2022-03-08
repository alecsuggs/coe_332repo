import json
import math

with open('sites.json', 'r') as f:
    siteinfo = json.load(f)

radius = 3389.5  ##kilometers
robot = [16.0, 82.0]  ##inital lat, lon
totalt = 0
for i in range(5):
    lat = siteinfo['sites'][i]['latitude']
    lon = siteinfo['sites'][i]['longitude']
    angle = math.acos(
        math.sin(math.radians(robot[0])) * math.sin(math.radians(lat)) + math.cos(math.radians(robot[0])) * math.cos(math.radians(lat)) * math.cos(math.radians(abs(robot[1] - lon))))
    d = radius * angle
    travel = d / 10
    if siteinfo['sites'][i]['composition'] == "stony":
        sample = 1
    if siteinfo['sites'][i]['composition'] == "iron":
        sample = 2
    if siteinfo['sites'][i]['composition'] == 'stony-iron':
        sample = 3
    totalt = totalt + travel + sample
    print("leg =", i, "travel time = ", travel, "sample time = ", sample)
    robot = [lat, lon]
print('total legs = ', i+1, "total time elapsed =", totalt)

