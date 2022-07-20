import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

@st.experimental_memo
def read_dataframe(input_data: str) -> pd.DataFrame:
    return pd.read_csv(input_data)

def main():
    # basic dashboard setup
    st.set_page_config(
        page_title="Real-Time Data Science Dashboard",
        page_icon="✅",
        layout="wide",
    )
    # input to be parameterized later
    input_data = "https://raw.githubusercontent.com/Lexie88rus/bank-marketing-analysis/master/bank.csv"
    
    # read the data
    df = read_dataframe(input_data)
  
    # dashboard title
    st.title("Real-Time / Live Data Science Dashboard")
    
    # job filter
    job_filter = st.selectbox("Select the job", pd.unique(df['job']))
    
    # dataframe filter
    df = df[df["job"] == job_filter]
    
    # near real-time / live feed simulation
    placeholder = st.empty()
    for seconds in range(200):
        df["age_new"] = df["age"] * np.random.choice(range(1, 5))
        df["balance_new"] = df["balance"] * np.random.choice(range(1, 5))

        # creating KPIs
        avg_age = np.mean(df["age_new"])
        count_married = int(
            df[(df["marital"] == "married")]["marital"].count()
            + np.random.choice(range(1, 30))
        )
        balance = np.mean(df["balance_new"])
        with placeholder.container():
            # create three columns
            kpi1, kpi2, kpi3 = st.columns(3)

            # fill in those three columns with respective metrics or KPIs
            kpi1.metric(
                label="Age ⏳",
                value=round(avg_age),
                delta=round(avg_age) - 10,
            )
            kpi2.metric(
                label="Married Count 💍",
                value=int(count_married),
                delta=-10 + count_married,
            )
            kpi3.metric(
                label="A/C Balance ＄",
                value=f"$ {round(balance,2)} ",
                delta=-round(balance / count_married) * 100,
            )
            # create two columns for charts
            fig_col1, fig_col2 = st.columns(2)
            with fig_col1:
                st.markdown("### First Chart")
                fig = px.density_heatmap(
                    data_frame=df, y="age_new", x="marital"
                )
                st.write(fig)

            with fig_col2:
                st.markdown("### Second Chart")
                fig2 = px.histogram(data_frame=df, x="age_new")
                st.write(fig2)

            st.markdown("### Detailed Data View")
            st.dataframe(df)
            time.sleep(1)

if __name__ == "__main__":
    main()