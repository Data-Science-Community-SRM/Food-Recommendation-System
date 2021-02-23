import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np 

st.title("FOOOD Predictor")
st.text("just to try out")
st.image("foood.jpg")

## nav = st.sidebar.radio("Navigation",["Home","IF Necessary 1","If Necessary 2"])

st.subheader("Whats your preference?")
vegn = st.radio("Vegetables or none!",["veg","non-veg"],index = 1) 

st.subheader("What Cuisine do you prefer?")
cuisine = st.selectbox("Choose your favourite!",['Healthy Food', 'Snack', 'Dessert', 'Japanese', 'Indian', 'French',
       'Mexican', 'Italian', 'Chinese', 'Beverage', 'Thai'])


st.subheader("How well do you want the dish to be?")  #RATING
val = st.slider("from poor to the best!",0,10)

food = pd.read_csv("../input/food.csv")
ratings = pd.read_csv("../input/reviews.csv")
combined = pd.merge(ratings, food, on='Food_ID')
#ans = food.loc[(food.C_Type == cuisine) & (food.Veg_Non == vegn),['Name','C_Type','Veg_Non']]

ans = combined.loc[(combined.C_Type == cuisine) & (combined.Veg_Non == vegn)& (combined.Review >= val),['Name','C_Type','Veg_Non']]
names = ans['Name'].tolist()
x = np.array(names)
ans1 = np.unique(x)

bruh = st.checkbox("Do you want to see our selection?")
if bruh == True:
    finallist = st.selectbox("Our Choices",ans1)



