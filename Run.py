from Libraries import *
import streamlit as st

st.write("Thisath's")
countries = ["Sri Lanka","India","United Kingdom","United Sates of America","Canada","Australia","China","Spain","Bangladesh","Italy"]
data_types = ["cases","deaths","recovered"]
flagcodes = {'Sri Lanka' : 'lk', 'India' : 'in', 'United Kingdom' : 'gb', 'United States of America' : 'us', 'Canada' : 'ca', 'Australia' : 'au', 'China' : 'cn','Spain' : 'es', 'Bangladesh' : 'bd', 'Italy' : 'it'}
country = st.sidebar.selectbox('Pick a country', countries)
days = st.sidebar.slider('Select how many days you want to see', min_value=1, max_value=90, step=1)
data_type = st.sidebar.multiselect('Pick one or more data types', data_types)

total_cases = get_historic_cases(country,str(days))
total_deaths = get_historic_deaths(country,str(days))
total_rec = get_historic_recoveries(country,str(days))
#total_df = pd.concat([total_cases, total_deaths, total_rec], axis=1).astype(int)

yesterday_cases = get_yesterday_cases(country)
yesterday_deaths = get_yesterday_deaths(country)
yesterday_rec = get_yesterday_recoveries(country)
#yesterday_df = pd.concat([yesterday_cases, yesterday_deaths, yesterday_rec], axis=1).astype(int)

daily_cases = get_daily_cases(country,str(days))
daily_deaths = get_daily_deaths(country,str(days))
daily_rec = get_daily_recoveries(country,str(days))
daily_df = pd.concat([daily_cases, daily_deaths, daily_rec], axis=1).astype(int)
st.title("Covid-19 Dashboard")
st.metric("Selected Country-",country)
st.image(f"https://flagcdn.com/80x60/{flagcodes[country]}.png")
#st.metric("Cases from Yesterday - ", yesterday_cases)
#st.metric("Deaths from Yesterday - ", yesterday_deaths)
#st.metric("Recoveries from Yesterday - ", yesterday_rec)
col1,col2,col3 = st.columns(3)
col1.metric("Cases from Yesterday - ", yesterday_cases)
col2.metric("Deaths from Yesterday - ", yesterday_deaths)
col3.metric("Recoveries from Yesterday - ", yesterday_rec)
st.line_chart(daily_df)
st.video('https://www.youtube.com/watch?v=BtN-goy9VOY')
st.write("Thank you for using my website! Stay Safe!")