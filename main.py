import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu


with open('./style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.markdown("<h1 class='main-title'>Mini Challenge - Week 4 - Day 2</h1>", unsafe_allow_html=True)

df = pd.read_csv("./f1_results_2024.csv")

menu_selected = option_menu(None, ["Laps", "Drivers", "Top Drivers", 'Constructors'],
    icons=['house', 'cloud-upload', "list-task", 'gear'],
    menu_icon="cast",
    default_index=0,
    orientation="vertical",
    styles={
        "icon": {
            "color": "#00000",
            "font-size": "16px"
        },
        "nav-link": {
            "font-size": "16px",
            "text-align": "left",
            "margin":"0px",
            "--hover-color": "#f0000"
        },
        "nav-link-selected": {
            "background-color": "#f0000"
        }
    }
)

match menu_selected:
    case "Laps":
        fig = px.bar(
            df,
            x="race_name",
            y="fastestLap",
            title="Number of Fastest Laps by Race",
            labels={
                "fastestLap": "Fastest Lap",
                "race_name": "Race"
            }
        )

        st.plotly_chart(fig, use_container_width=True)
    case "Drivers":
        fig = px.scatter(
            df,
            x="driver_name",
            y="points",
            title="Points Per Driver",
            labels={
                "points": "Points",
                "driver_name": "Driver Name"
            },
            color="driver_name"
        )

        st.plotly_chart(fig, use_container_width=True)
    case "Top Drivers":
        top_10_points = df.groupby("driver_name")["points"].sum().sort_values(ascending=False).head(10).reset_index()

        fig = px.bar(
            top_10_points,
            x="driver_name",
            y="points",
            title="Top 10 Drivers With The Most Points",
            labels={"points": "Points", "driver_name": "Driver Name"},
            color="driver_name"
        )

        st.plotly_chart(fig, use_container_width=True)
    case "Constructors":
        fig = px.bar(
            df,
            x="constructor_name",
            y="points",
            title="Constructors' Points",
            labels={
                "points": "Points",
                "constructor_name": "Constructor Name"
            },
            color="constructor_name"
        )

        st.plotly_chart(fig, use_container_width=True)
