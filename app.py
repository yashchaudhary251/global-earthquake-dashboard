import streamlit as st
from earthquake_data import get_earthquake_data
import folium
from streamlit_folium import st_folium
import plotly.express as px

st.set_page_config(
    page_title="Earthquake Dashboard",
    layout="wide"
)

# PAGE TITLE


st.title("🌍 Global Earthquake Dashboard")


st.sidebar.header("🎛️ Filters")


min_mag = st.sidebar.slider(
    "Minimum Magnitude",
    min_value=0.0,
    max_value=10.0,
    value=2.0,
    step=0.1
)
depth_range = st.sidebar.slider(
    "Depth Range (km)",
    min_value=0,
    max_value=700,
    value=(0, 700)
)
st.sidebar.write(depth_range)


st.sidebar.success(
    f"""
Magnitude ≥ {min_mag}

Depth: {depth_range[0]} km - {depth_range[1]} km
"""
)

    
    
# LOAD DATA


df = get_earthquake_data()


# FILTERS



filtered_df = df[
    (df["mag"] >= min_mag)
    &
    (df["depth"] >= depth_range[0])
    &
    (df["depth"] <= depth_range[1])
]


# METRICS


total_eq = len(filtered_df)
strongest_mag = filtered_df["mag"].max()
avg_mag = round(filtered_df["mag"].mean(), 2)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Earthquakes", total_eq)

with col2:
    st.metric("Strongest Magnitude", strongest_mag)

with col3:
    st.metric("Average Magnitude", avg_mag)

# ==========================================
# TOP 5 EARTHQUAKES
# ==========================================

st.markdown("Top 5 Strongest Earthquakes")

top5 = filtered_df.sort_values(
    by="mag",
    ascending=False
).head(5)

st.dataframe(top5)


# ==========================================
# FOLIUM MAP
# ==========================================


st.subheader("🌍 Earthquake Map")

m = folium.Map(
    location=[0, 0],
    zoom_start=2,
    tiles="CartoDB dark_matter"
)

for index, row in filtered_df.iterrows():

    mag = row["mag"]

    if mag < 2:
        color = "green"
    elif mag < 4:
        color = "orange"
    else:
        color = "red"

    folium.CircleMarker(
        location=[row["latitude"], row["longitude"]],
        radius=mag * 2,
        popup=f'{row["place"]} | Magnitude {mag}',
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7
    ).add_to(m)

st_folium(
    m,
    use_container_width=True,
    height=650
)



# ==========================================
# DATASET INFO
# ==========================================
st.subheader("📊 Magnitude Distribution")

fig = px.histogram(
    filtered_df,
    x="mag",
    nbins=15,
    color_discrete_sequence=["#FF4B4B"]
)

fig.update_traces(
    hovertemplate=
    "<b>Magnitude Range</b><br>" +
    "%{x}<br>" +
    "<b>Earthquakes:</b> %{y}<extra></extra>"
)
fig.update_layout(
    bargap=0.05
)
fig.update_layout(
    xaxis_title="Magnitude",
    yaxis_title="Number of Earthquakes"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

shallow = len(
    filtered_df[
        filtered_df["depth"] < 70
    ]
)

intermediate = len(
    filtered_df[
        (filtered_df["depth"] >= 70)
        &
        (filtered_df["depth"] < 300)
    ]
)

deep = len(
    filtered_df[
        filtered_df["depth"] >= 300
    ]
)

st.subheader("🌋 Depth Analysis")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Shallow (0-70 km)",
        shallow
    )

with col2:
    st.metric(
        "Intermediate (70-300 km)",
        intermediate
    )

with col3:
    st.metric(
        "Deep (300+ km)",
        deep
    )


st.markdown("---")
st.caption(
    "Data Source: USGS Earthquake API | Built with Streamlit, Pandas, Folium and Plotly"
)




