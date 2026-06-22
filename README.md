# Global Earthquake Dashboard

A simple earthquake monitoring dashboard built using Streamlit, Pandas, Folium, and Plotly.

The dashboard fetches real-time earthquake data from the USGS Earthquake API and provides an interactive way to explore recent seismic activity around the world.

## Features

* Live earthquake data from the USGS API
* Interactive world map with earthquake markers
* Magnitude filtering
* Depth filtering
* Summary metrics (total earthquakes, strongest magnitude, average magnitude)
* Top 5 strongest earthquakes table
* Magnitude distribution histogram
* Earthquake depth analysis
* Responsive dashboard layout

## Tech Stack

* Python
* Streamlit
* Pandas
* Folium
* Plotly
* Requests

## Project Structure

```text
.
├── app.py
├── earthquake_data.py
├── requirements.txt
└── README.md
```

## How It Works

The application pulls the latest earthquake data from the USGS GeoJSON feed.

After loading the data, the dashboard:

1. Extracts important fields such as magnitude, location, depth, coordinates, and timestamp.
2. Applies user-selected filters.
3. Calculates summary statistics.
4. Displays the results using tables, charts, and an interactive map.

## Running Locally

Clone the repository:

```bash
git clone <your-repository-url>
cd Global-Earthquake-Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
streamlit run app.py
```

The dashboard will open in your browser automatically.

## Data Source

USGS Earthquake Hazards Program

https://earthquake.usgs.gov

## What I Learned

This project helped me get hands-on experience with:

* Working with REST APIs
* Processing JSON data
* Building dashboards with Streamlit
* Interactive mapping using Folium
* Data visualization with Plotly
* Creating filter-based analytical dashboards

## Future Improvements

Some ideas for future versions:

* Country-level earthquake analysis using GeoPandas
* Historical earthquake trends
* Automatic refresh of live data
* Additional map layers
* Earthquake alerts for specific magnitude thresholds

## Screenshot

Add screenshots of the dashboard here after deployment.

---

Built as a GIS and Data Analytics learning project.
