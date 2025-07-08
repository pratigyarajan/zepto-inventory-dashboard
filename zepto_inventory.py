import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

df=pd.read_csv("zepto_v2.csv",encoding="ISO-8859-1")

st.title(" welcome to Zepto Inventory..,!")
Category=st.selectbox("Our Zepto Products...!",df['Category'].unique())
filtered=df[df["Category"]==Category]

st.write(filtered.groupby("name")[["mrp","discountPercent"]].sum())


fig, ax = plt.subplots()
sns.boxplot(x='quantity', y='discountedSellingPrice', data=filtered, ax=ax)
st.pyplot(fig)