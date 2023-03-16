import streamlit as st

# Define the keys in the dictionary
keys = ["key1", "key2", "key3"]

# Initialize an empty dictionary with the keys
my_dict = dict.fromkeys(keys)

# Define the dropdown options
dropdown_options = ["Option 1", "Option 2", "Option 3"]

# Create a form for the user to input values for the keys
with st.form("my_form"):
    # Add a dropdown for the user to select a key
    key = st.selectbox("Select a key:", keys)

    # Add a dropdown for the user to select a value
    value = st.selectbox("Select a value:", dropdown_options)

    # Add a submit button to submit the form
    submit_button = st.form_submit_button(label="Submit")

    # Update the dictionary with the user's input if the form is submitted
    if submit_button:
        my_dict[key] = value

# Print the populated dictionary
st.write("Populated Dictionary:", my_dict)

# run the app
