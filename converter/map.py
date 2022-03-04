import csv
import json
import argparse
from os.path import exists

parser = argparse.ArgumentParser()                                               

parser.add_argument("--file", "-f", type=str, required=True)
args = parser.parse_args()

file_exists = exists(args.file)
if(file_exists == False):
  print('file not found')
  exit()

csvFile = open("data.csv", "r")

jsonData = {
  "type": "featureCollection",
  "features": []
} 

features = []

csvFile = csv.reader(csvFile)
for row in csvFile:
  jsonData['features'].append({
    "type": "Feature",
    "geometry": {
      'type': 'Point',
      'coordinates': [float(row[0]), float(row[1])]
    },
    'properties': {
      'title': row[2],
      'description': row[3]
    },
  })

jsonFile = open("map.json", "w")
jsonFile.write(json.dumps(jsonData)+"\n")
jsonFile.close()
