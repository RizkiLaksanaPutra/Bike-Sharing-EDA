import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import streamlit as st

df_day = pd.read_csv('data/cleaned_df_day.csv')
df_hour = pd.read_csv('data/cleaned_df_hour.csv')

df_day.reset_index(inplace = True)
df_hour.reset_index(inplace = True)
weekday_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
df_day['month'] = pd.Categorical(df_day['month'], categories=month_order, ordered=True)
df_day['weekday'] = pd.Categorical(df_day['weekday'], categories=weekday_order, ordered=True)

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
    sns.barplot(x = "weekday", y = "count", data = df_day, hue = 'year', ax = ax, order = weekday_order)
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


def create_monthly_df(df):
    monthly_df = df_day.groupby(by='month').agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    return monthly_df

def create_weekday_df(df):
    weekday_df = df_day.groupby(by='weekday').agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    return weekday_df

def create_hour_df(df):
    hour_df = df_hour.groupby(by='hour').agg({
        'casual': 'sum',
        'registered': 'sum',
    })
    return hour_df

monthly_df = create_monthly_df(df_day)
weekday_df = create_weekday_df(df_day)
hour_df = create_hour_df(df_hour)

st.subheader('Apa saja bulan, hari, dan jam tersibuk untuk bike sharing berdasarkan kategori pengguna?')
user_tab1, user_tab2, user_tab3 = st.tabs(["Bulan", "Hari", "Jam"])
with user_tab1:
    fig, ax = plt.subplots(figsize=(10, 5))
    monthly_df.plot(kind='bar', stacked=True, ax=ax)
    plt.title('Jumlah pengguna bike sharing berdasarkan bulan dan kategori pengguna')
    plt.xlabel('Month')
    plt.ylabel('Count')
    plt.legend(loc='upper right')
    st.pyplot(fig)

with user_tab2:
    fig, ax = plt.subplots(figsize=(10, 5))
    weekday_df.plot(kind='bar', stacked=True, ax=ax)
    plt.title('Jumlah pengguna bike sharing berdasarkan bulan dan kategori pengguna')
    plt.xlabel('Weekday')
    plt.ylabel('Count')
    plt.legend(loc='upper right')
    st.pyplot(fig)

with user_tab3:
    fig, ax = plt.subplots(figsize=(10, 5))
    hour_df.plot(kind='bar', stacked=True, ax=ax)
    plt.title('Jumlah pengguna bike sharing berdasarkan bulan dan kategori pengguna')
    plt.xlabel('Hour')
    plt.ylabel('Count')
    plt.legend(loc='upper right')
    st.pyplot(fig)

st.subheader('Apa saja bulan, hari, dan jam tersibuk untuk bike sharing berdasarkan musim?')
season_tab1, season_tab2, season_tab3 = st.tabs(["Bulan", "Hari", "Jam"])
with season_tab1:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "month", y = "count", data = df_day, hue = 'season', ax = ax)
    ax.set_xlabel('Month')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan bulan dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with season_tab2:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "weekday", y = "count", data = df_day, hue = 'season', ax = ax, order = weekday_order)
    ax.set_xlabel('Weekday')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan hari dan tahun', loc = 'center')
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

with season_tab3:
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x = "hour", y = "count", data = df_hour, hue = 'season', ax = ax)
    ax.set_xlabel('Hour')
    ax.set_ylabel('Count')
    ax.set_title('Jumlah pengguna bike sharing berdasarkan jam dan tahun', loc = 'center')
    st.pyplot(fig)

st.subheader('Apakah ada perbedaan yang signifikan dalam penggunaan bike sharing pada hari kerja dan hari libur?')
fig, ax = plt.subplots(figsize=(10, 5))
sns.countplot(x = 'holiday', data = df_day, palette='viridis')
plt.title('Jumlah pengguna bike sharing berdasarkan hari kerja dan hari libur')
plt.xlabel('Holiday?')
plt.ylabel('Count')
st.pyplot(fig)

st.subheader('Musim apa dengan jumlah pengguna bike share tertinggi?')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x = 'season', y = 'count', data = df_day, hue = 'season')
plt.title('Jumlah pengguna bike sharing berdasarkan musim')
plt.xlabel('Season')
plt.ylabel('Count')
st.pyplot(fig)

st.subheader('Bagaimana pengaruh cuaca dengan jumlah pengguna bike share?')
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x = 'weathersit', y = 'count', data = df_hour, hue = 'weathersit')
plt.title('Jumlah pengguna bike sharing berdasarkan cuaca')
plt.xlabel('Weather')
plt.ylabel('Count')
st.pyplot(fig)