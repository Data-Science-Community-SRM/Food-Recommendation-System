import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 

st.title("FOOOD Predictor")
st.text("just to try out")
st.image("foood.jpg")

nav = st.sidebar.radio("Navigation",["Home","IF Necessary 1","If Necessary 2"])

st.subheader("What Cuisine do you prefer?")
cuisine = st.selectbox("Choose your favourite!",["Indian","Chinese","Continental","Middle Eastern",
"Japenese"])

st.subheader("Whats your preference?")
vegn = st.radio("Vegetables or none!",["veg","non-veg"],index = 1)

#bruh = st.checkbox("you accept the T&C") gives boolean value

st.subheader("How much do you like the dish?")  #RATING
val = st.slider("from poor to the best!",0,10)

#veg nonver
#cuisine
#rating
#display the food name data accordingly
#dark mode

#st.write(foods)
