import streamlit as st
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import io   
import re
from datetime import datetime
import pytz
from lib_func import save_text_from_url
from lib_func import convert_utc_to_edt
from lib_func import convert_forecast_to_df
from lib_func import plot_forecast

#3-day forecast
url_forecast = 'https://services.swpc.noaa.gov/text/3-day-forecast.txt'

#File name
filename_forecast = 'solar_forecast.txt'
time_zones = pytz.all_timezones
opt_selected = 'US/Pacific'
#forecast_df = convert_forecast_to_df(filename_forecast, 'US/Pacific')
forecast_df = convert_forecast_to_df(filename_forecast, opt_selected)
f = plot_forecast(forecast_df, 'US/Pacific', ret= True )
st.write("""
         # Aurora forecast
         """)
st.pyplot(f)