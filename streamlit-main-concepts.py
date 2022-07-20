# references
# https://docs.streamlit.io/library/get-started/main-concepts
# https://plotly.com/python/plotly-express/

# don't forget to run this following command in terminal
# streamlit run <file_name>.py

# create a table
import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

# Task 1: Create a table
def show_dataframe():
    # show a table directly with pandas dataframe
    df = pd.DataFrame({
        "first_column": range(1, 5, 1),
        "second_column": range(10, 50, 10)
    })
    df
    
def show_dataframe():
    # using st.write command
    st.write("Simple table:")
    st.write(
        pd.DataFrame({
            "first_column": range(1, 5, 1),
            "second_column": range(10, 50, 10)
        })
    )
    
def show_dataframe():
    # using st.dataframe command
    df = np.random.randn(10, 5)
    st.dataframe(df)

def show_dataframe():
    # using pandas styler object
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5))
    )
    # indicate the highest number
    st.dataframe(df.style.highlight_max(axis=0))
    
def show_dataframe():
    # static table generation
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5))
    )
    st.dataframe(df)

# Task 2: Line chart
def line_chart():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)
    
def px_line_chart():
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    fig = px.line(
        chart_data, 
        x=chart_data.index, 
        y="a", 
        markers=True,
        title="Simple line chart"
    )
    st.write(fig)

# Task 3: Plot a map
def plot_sf_map():
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['latitude', 'longitude']
    )
    st.map(map_data)

# Task 4: Widgets
def slider():
    # this is a widget
    x = st.slider('x')
    st.write(x, 'squared is', x**2)

def print_the_input():
    st.text_input("Your name", key="name")
    st.session_state.name

if __name__ == "__main__":
    print_the_input()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    