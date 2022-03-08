import json

siteinfo = {
  "sites" :  [
    {
      "site_id": 1,
      "latitude": 16.23335423897241,
      "longitude": 84.22567946311249,
      "composition": "iron"
    },
    {
      "site_id": 2,
      "latitude": 16.714833623042153,
      "longitude": 82.84554246756586,
      "composition": "stony-iron"
    },
    {
      "site_id": 3,
      "latitude": 18.12454521232142,
      "longitude": 83.61321478552142,
      "composition": "stony"
    },
    {
      "site_id": 4,
      "latitude": 17.99648752134562,
      "longitude": 83.22388965478551,
      "composition": "stony"
    },
    {
      "site_id": 5,
      "latitude": 18.65663245712412,
      "longitude": 82.56324784112198,
      "composition": "stony-iron"
    }
   ]
}

with open('sites.json','w') as out:
    json.dump(siteinfo, out, indent = 2)
