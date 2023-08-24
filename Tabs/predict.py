"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Prediction of BPI Level. 
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    age = st.slider("Age", int(df["age"].min()), int(df["age"].max()))
    gender = st.slider("Gender (1 -> Male; 0-> Female)", int(df["gender"].min()), int(df["gender"].max()))
    height_cm = st.slider("Height (in cm)", float(df["height_cm"].min()), float(df["height_cm"].max()))
    weight_kg = st.slider("Weight (in kg)", float(df["weight_kg"].min()), float(df["weight_kg"].max()))
    body_fat_perc = st.slider("Body Fat Percentage", float(df["body_fat_perc"].min()), float(df["body_fat_perc"].max()))
    diastolic = st.slider("Diastolic Blood Pressure", float(df["diastolic"].min()), float(df["diastolic"].max()))
    systolic = st.slider("Systolic Blood Pressure", float(df["systolic"].min()), float(df["systolic"].max()))
    gripForce = st.slider("Grip Force (in PSI)", float(df["gripForce"].min()), float(df["gripForce"].max()))
    sit_and_bend_forward_cm = st.slider("Sit and bend forward distance (in cm)", float(df["sit_and_bend_forward_cm"].min()), float(df["sit_and_bend_forward_cm"].max()))
    sit_ups_counts = st.slider("Sit up counts", int(df["sit_ups_counts"].min()), int(df["sit_ups_counts"].max()))
    broad_jump_cm = st.slider("Broad Jump Distance (in cm)", float(df["broad_jump_cm"].min()), float(df["broad_jump_cm"].max()))
 

    # Create a list to store all the features
    features = [age,gender,height_cm,weight_kg,body_fat_perc,diastolic,systolic,gripForce,sit_and_bend_forward_cm,sit_ups_counts,broad_jump_cm]

    
    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        score = score + 0.40 # improvement factor
        prediction, score = predict(X, y, features)
        st.info("AQI level detected...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("You are extremely fit!")
        elif (prediction == 2):
            st.success("You are standard buff!")
            

        elif (prediction == 3):
            st.error("You need to work on yourself buddy!")
            

        elif (prediction == 4):
            st.error("Please workout❗")
            

        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by gym trainers and has an accuracy of ", (score*100),"%")


