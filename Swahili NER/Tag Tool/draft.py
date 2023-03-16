import streamlit as st
import pandas as pd
import random
import os
# ------------------------------------------------------------------------------------
# CONSTANTS

df_file = 'sdata.csv'
sentence_file = 'RFI April - Novmber 2022 titles - cleaned.txt'

# ------------------------------------------------------------------------------------
# Read txt file with sentences, without '\n'
with open(sentence_file, 'r') as f:
    sentences = f.read().split('\n')


# ------------------------------------------------------------------------------------
# A function to select a random sentence and 6 random words from the sentence
def random_selection():
    select_sent = sentences[random.randint(0, len(sentences))]

    all_words = select_sent.split()
    if len(all_words) < 6:      # this is to ensure that the sentence has more than 6 words, if not, it will return None
        return None
    else:
        select_words = random.sample(all_words, k=min(len(all_words), 3))
        return select_sent, select_words
    

# ------------------------------------------------------------------------------------
# Streamlit app
def main():
    # Define the list of items to process
    sent , items = random_selection()


    # title and sentence
    st.markdown("<h1 style='text-align: center;'>NER Taging Tool</h1>", unsafe_allow_html=True)
    st.markdown("-----")

    st.markdown("<u>Generated / Selected Sentence</u>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify;'>{sent}</p>", unsafe_allow_html=True)
    st.markdown("-----")

    if not os.path.isfile(df_file):
        # Create a new dataframe
        df = pd.DataFrame(columns=['Sentence', 'Tags'])
    else:
        # load existing data
        df = pd.read_csv(df_file)

    # define the dropdown options
    dropdown_options = ["", "PERSON", "NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT", "WORK_OF_ART", "LAW", 
                        "LANGUAGE", "DATE", "TIME", "PERCENT", "MONEY", "QUANTITY", "ORDINAL", "CARDINAL"]

    # Create a list to store new tags, this will extend the existing data
    

    
    # Create a form for user inputs
    with st.form(key='tag_form'):
        new_tags = []
        for i, item in enumerate(items):
            st.write(f"Enter an NER Tag for: {item}:")
            value = st.selectbox("Select a tag", dropdown_options, key=i)
            new_tags.append({item: value})
        
        # Add a submit button to the form
        submitted = st.form_submit_button('Submit')

        # If the form is submitted, append the new tags to the dataframe
        if submitted:
            df = df.append({'Sentence': sent, 'Tags': new_tags}, ignore_index=True)

            # Save the dataframe
            df.to_csv(df_file, index=False)
            st.success("Data saved successfully!")
    
    # if the form is not submitted, display the current tags
    if not submitted:
        for tag in new_tags:
            for key, value in tag.items():
                st.write(f"{key}: {value}")



if __name__ == "__main__":
    main()
