import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Uber Pickups in NYC')

# Load data
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    data.rename(lambda x: str(x).lower(), axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Load 10,000 rows of data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text('Loading data...done!')

# Display raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Display histogram of the number of pickups by hour
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Display map of all pickups
st.subheader('Map of all pickups')
st.map(data)

# Filter data by hour
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# Display map of filtered pickups
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)