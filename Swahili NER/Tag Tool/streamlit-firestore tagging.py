import streamlit as st
import random
import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# FIRE STORE DB
cred = credentials.Certificate("credentials.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

# CONSTANTS
#df_file = 'sdata.csv'
sentence_file = 'Data/RFI April - Novmber 2022 titles - cleaned.txt'

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Read txt file with sentences, without '\n'
with open(sentence_file, 'r') as f:
    sentences = f.read().split('\n')


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# A function to select a random sentence and 6 random words from the sentence
def random_selection():
    select_sent = sentences[random.randint(0, len(sentences))]

    all_words = select_sent.split()
    if len(all_words) < 6:      # this is to ensure that the sentence has more than 6 words, if not, it will return None
        return None
    else:
        select_words = random.sample(all_words, k=min(len(all_words), 3))
        return select_sent, select_words
    

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Stream-lit app
def main():
    # Define the list of items to process
    sent , items = random_selection()

    # title and sentence
    st.markdown("<h1 style='text-align: center;'>NER Taging Tool</h1>", unsafe_allow_html=True)
    st.markdown("-----")

    st.markdown("<u>Generated / Selected Sentence</u>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: justify;'>{sent}</p>", unsafe_allow_html=True)
    st.markdown("-----")

    # define the dropdown options
    dropdown_options = ["PERSON", "ORG", "LOC", "PRODUCT", "EVENT", 
                        "LANGUAGE", "DATE", "TIME", "MONEY", "NUMBER"]

    

    # Create a form for user inputs
    with st.form(key='tag_form'):

        new_tags = []

        for i, item in enumerate(items):
            st.write(f"Enter an NER Tag for: {item}:")
            value = st.selectbox("Select a tag", dropdown_options, key=i)
            new_tags.append({item: value})
        
        # Add a submit button to the form
        submitted = st.form_submit_button('Submit')

        # If the form is submitted, write the new tags to Firestore
        if submitted:
            # Define the Firestore document ID as a combination of the sentence and a timestamp
            doc_id = f"{sent}_{int(time.time())}"
            
            # Define the document data
            doc_data = {
                'sentence': sent,
                'tags': new_tags
            }
            
            # Write the document to Firestore
            db.collection('ner_tags').document(doc_id).set(doc_data)

            st.success("Data saved successfully!")

            # Reset the form
            new_tags = []
    

    # ------------------------------------------------------------------------------------

    st.markdown('---')
    st.write("For reference, the possible tags are described below:")
    st.write("PERSON: People, including fictional.", 
             "NORP: Nationalities or religious or political groups.", 
             "FAC: Buildings, airports, highways, bridges, etc.", 
             "ORG: Companies, agencies, institutions, etc.", 
             "GPE: Countries, cities, states.", 
             "LOC: Non-GPE locations, mountain ranges, bodies of water.", 
             "PRODUCT: Objects, vehicles, foods, etc. (Not services.)", 
             "EVENT: Named hurricanes, battles, wars, sports events, etc.", 
             "WORK_OF_ART: Titles of books, songs, etc.", 
             "LAW: Named documents made into laws.", 
             "LANGUAGE: Any named language.", 
             "DATE: Absolute or relative dates or periods.", 
             "TIME: Times smaller than a day.", 
             "PERCENT: Percentage, including ”%“.", 
             "MONEY: Monetary values, including unit.", 
             "QUANTITY: Measurements, as of weight or distance.", 
             "ORDINAL: “first”, “second”, etc.", 
             "CARDINAL: Numerals that do not fall under another type.")


if __name__ == "__main__": 
    main()
