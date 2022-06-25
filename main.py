import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import statsmodels.api as sm
from datetime import timedelta
import datetime


def seasonal_decompose(y):
    decomposition = sm.tsa.seasonal_decompose(y, model='additive', extrapolate_trend='freq')
    return pd.DataFrame(decomposition.__dict__)


def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )


def convert_df(df):
    return df.to_csv().encode('utf-8')


# force screen width
_max_width_()

st.title("Data Mime")
data = None
st.sidebar.title("data parameters")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    data = pd.read_csv(uploaded_file, sep=";")
    st.write(data)
    # Select time variable
    time_variable = st.sidebar.selectbox('Time variable', ['date_debut', *data.columns])
    options = st.sidebar.multiselect('Sub samples', data.columns, ['nom_poll', 'nom_com', 'code_station'])
    value = st.sidebar.selectbox('Value', ['valeur', *data.columns])
    st.sidebar.subheader("New data settings")
    integer = st.sidebar.checkbox('Integer')
    positive = st.sidebar.checkbox('Positive')
    start_date = st.sidebar.date_input("Start date")
    end_date = st.sidebar.date_input("End date")

if time_variable and options and value:
    data["date_debut"] = pd.to_datetime(data["date_debut"])
    st.subheader("Dataset Description")
    with st.expander("Data exploration"):
        i = 0
        for key, df in data.set_index(time_variable).groupby(options)[value]:
            fig = px.line(df, x=df.index, y=df)
            fig.update_layout(template="ggplot2", title=str(key))
            st.plotly_chart(fig)
            i = i + 1
            if i > 6:
                break

    concat_df = []
    delta = datetime.timedelta(days=1)
    for key, df in data.set_index(time_variable).groupby(options)[value]:
        fit = seasonal_decompose(pd.Series(df, index=df.index))
        start = fit["_seasonal"].index[0]
        start_1 = fit["_seasonal"].index[1]
        end = start + timedelta(days=1)
        season = fit._seasonal[start_1:end]

        times = season.index.strftime("%H:%M:%S")

        current_date = start_date
        full_index = []
        nb_jour = 0
        while current_date < end_date:
            current_date += delta
            nb_jour = nb_jour + 1
            full_index.extend((current_date.strftime("%Y-%m-%d") + " " + times).to_list())
        # st.write(full_index)
        season_days = pd.concat([season] * nb_jour)
        new = season_days + fit["_trend"].mean() + fit["_resid"].sample(season_days.shape[0], replace=True).values

        if integer:
            new = new.apply(np.round).apply(int)

        if positive:
            new = np.where(new < 0, 0, new)
        df = pd.DataFrame({value: new}, index=full_index)
        for i, option in enumerate(options):
            df[option] = key[i]
        concat_df.append(df)

    final = pd.concat(concat_df, axis=0)
    final.index = pd.to_datetime(final.index)
    final = final.sort_index()
    csv = convert_df(final)

    st.write(final)
    st.sidebar.download_button(
        "Download new dataset",
        csv,
        "news.csv",
        "text/csv",
        key='download-csv'
    )

    i = 0
    for key, df in final.groupby(options)[value]:
        fig = px.line(x= df.index, y=df)
        fig.update_layout(template="ggplot2", title=str(key))
        st.plotly_chart(fig)
        i = i + 1
        if i > 6:
            break
