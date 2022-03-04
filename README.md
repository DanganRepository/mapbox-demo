# Mapbox Demo

#### Map Demo

1. Sign up for a Mapbox account and get a [Mapbox API Token](https://docs.mapbox.com/help/getting-started/access-tokens/)
2. In demo.html, replace `{{token}}` with your access token
3. Open demo.html in your browser

#### Map Converter

To convert a .csv to a mapbox geojson formatted .json file 
Note: the converter uses [Python 3](https://www.python.org/)

1. Add your CSV data to the `data.csv` file
2. Open a terminal, go to the `map.py` script and run `python3 map.py --file data.csv`
3. The data will be written to the map.json file
4. You can then update the json data into demo.html by changing the value of the `geojson` variable.

#### Sources

The full tutorial for this demo is [here](https://docs.mapbox.com/help/tutorials/custom-markers-gl-js/)

The projection used is 'equalEarth'. More projections can be found [here](https://docs.mapbox.com/mapbox-gl-js/guides/projections/)

The style used is 'outdoors-v11'. More Styles can be found [here](https://docs.mapbox.com/api/maps/styles/)
