import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("🏥 Healthcare Patient Analytics Dashboard")

# Get files from deployed repo folder
files = os.listdir(".")

st.write("Files in repo:", files)

train_file = None
test_file = None

for f in files:
    if "train" in f.lower():
        train_file = f
    if "test" in f.lower():
        test_file = f

if not train_file or not test_file:
    st.error("Train or Test file not found in GitHub repo")
    st.stop()

train_df = pd.read_csv(train_file)
test_df = pd.read_csv(test_file)

df = pd.concat([train_df, test_df], ignore_index=True)
df = df.dropna()

st.success("Dataset Loaded Successfully")

st.write("Shape:", df.shape)

num_cols = df.select_dtypes(include=["int64", "float64"]).columns

for col in num_cols[:4]:
    st.subheader(f"📊 {col}")
    fig, ax = plt.subplots()
    ax.hist(df[col], bins=20)
    st.pyplot(fig)

if "Gender" in df.columns:
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    df["Gender"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

if "Disease" in df.columns:
    st.subheader("Disease Distribution")
    fig, ax = plt.subplots()
    df["Disease"].value_counts().head(10).plot(kind="bar", ax=ax)
    st.pyplot(fig)
