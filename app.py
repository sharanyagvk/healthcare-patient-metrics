

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("🏥 Healthcare Analytics Dashboard")

folder = r"C:\Users\Lenova\Desktop\health care"
files = os.listdir(folder)

train_file = [f for f in files if "train" in f.lower()][0]
test_file = [f for f in files if "test" in f.lower()][0]

train_df = pd.read_csv(os.path.join(folder, train_file))
test_df = pd.read_csv(os.path.join(folder, test_file))

df = pd.concat([train_df, test_df], ignore_index=True)
df = df.dropna()

st.success("Data Loaded")

st.write("Rows:", df.shape[0])

num_cols = df.select_dtypes(include=["int64", "float64"]).columns

st.subheader("📊 Numeric Data Graphs")

for col in num_cols[:5]:
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20)
    ax.set_title(col)
    st.pyplot(fig)

if "Gender" in df.columns:
    st.subheader("👥 Gender Distribution")
    fig, ax = plt.subplots()
    df["Gender"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

if "Disease" in df.columns:
    st.subheader("🦠 Disease Count")
    fig, ax = plt.subplots()
    df["Disease"].value_counts().head(10).plot(kind="bar", ax=ax)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)