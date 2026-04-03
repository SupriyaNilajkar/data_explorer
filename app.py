import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("📊 Data Explorer – Understand Your Dataset")

# Upload CSV
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.subheader("📁 Dataset Preview")
    st.dataframe(df.head())

    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found!")
    else:
        column = st.selectbox("🔍 Select Numeric Column", numeric_cols)

        if column:
            st.subheader("📈 Statistical Analysis")

            mean = df[column].mean()
            median = df[column].median()
            mode = df[column].mode()[0]
            variance = df[column].var()
            std_dev = df[column].std()
            min_val = df[column].min()
            max_val = df[column].max()

            # Display stats
            st.write(f"Mean: {mean}")
            st.write(f"Median: {median}")
            st.write(f"Mode: {mode}")
            st.write(f"Variance: {variance}")
            st.write(f"Standard Deviation: {std_dev}")
            st.write(f"Minimum: {min_val}")
            st.write(f"Maximum: {max_val}")

            # Histogram
            st.subheader("📊 Histogram / Distribution")

            fig, ax = plt.subplots()
            sns.histplot(df[column], kde=True, ax=ax)
            st.pyplot(fig)

            # Insights
            st.subheader("🧠 Insights")

            if mean > median:
                skew = "positively skewed (right skewed)"
            elif mean < median:
                skew = "negatively skewed (left skewed)"
            else:
                skew = "symmetrical"

            st.write(f"• The data is **{skew}**.")
            st.write(f"• Most values lie between {min_val} and {max_val}.")
            st.write(f"• Standard deviation is {round(std_dev,2)}, indicating spread of data.")
            st.write("• Histogram shows how data is distributed across ranges.")