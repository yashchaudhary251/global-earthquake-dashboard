import requests
import pandas as pd

def get_earthquake_data():

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson"

    response = requests.get(url)

    data = response.json()

    earthquakes = []

    for feature in data["features"]:

        mag = feature["properties"]["mag"]
        place = feature["properties"]["place"]

        time = pd.to_datetime(
            feature["properties"]["time"],
            unit="ms"
        )

        coords = feature["geometry"]["coordinates"]

        earthquakes.append({
            "mag": mag,
            "place": place,
            "time": time,
            "longitude": coords[0],
            "latitude": coords[1],
            "depth": coords[2]
        })

    return pd.DataFrame(earthquakes)