import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st

df_day = pd.read_csv('data/cleaned_df_day.csv')
df_hour = pd.read_csv('data/cleaned_df_hour.csv')

st.header('Dashboard EDA Bike Sharing')

st.subheader('Apa saja bulan, hari, dan jam tersibuk untuk bike sharing berdasarkan tahun?')
year_tab1, year_tab2, year_tab3 = st.tabs(["Bulan", "Hari", "Jam"])
with year_tab1:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "month", y = "count", data = df_day, hue = 'year', ax = ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan bulan dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with year_tab2:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "weekday", y = "count", data = df_day, hue = 'year', ax = ax)
    ax.set_xlabel('Weekday')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan hari dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with year_tab3:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "hour", y = "count", data = df_hour, hue = 'year', ax = ax)
    ax.set_xlabel('Hour')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan jam dan tahun', loc = 'center')
    st.pyplot(fig)



st.subheader('Apa saja bulan, hari, dan jam tersibuk untuk bike sharing berdasarkan kategori pengguna?')
user_tab1, user_tab2, user_tab3 = st.tabs(["Bulan", "Hari", "Jam"])
with user_tab1:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "month", y = "count", data = df_day, hue = 'year', ax = ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan bulan dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with user_tab2:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "weekday", y = "count", data = df_day, hue = 'year', ax = ax)
    ax.set_xlabel('Weekday')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan hari dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with user_tab3:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "hour", y = "count", data = df_hour, hue = 'year', ax = ax)
    ax.set_xlabel('Hour')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan jam dan tahun', loc = 'center')
    st.pyplot(fig)