"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Body Performance Index Detector")

    # Add image to the home page
    st.image('images/home.png')

    st.subheader("What is BPI ?")

    st.write("The performance index covers seven different functional areas and identifies those requiring a training strategy to improve performance or recover from an injury by using the data obtained from the high-performers assessed using the device as a benchmark.")
    
    
    st.write('The purpose of the BPI is to help people know how the local body index quality impacts their health.')
    

    
  
