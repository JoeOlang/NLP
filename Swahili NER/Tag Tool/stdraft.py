import streamlit as st
from streamlit import sidebar
import io
import pickle
import random

# -- FILES --
# -- Load In-built files (Pickle binary format) --
with open('Data/sw_sentences.pkl', 'rb') as f:
    sw_sentences = pickle.load(f)


# -- External Files --
# function to check if a file is a text file
def is_text_file(file):
    return file.type == 'text/plain'

# function to convert a text file to a list of sentences
def read_file(file):
    if file is None:
        return []
    with io.BytesIO(file.read()) as f:
        sentences = f.read().decode().split('\n')
    return sentences


# -- TAGGING --
# sentence selector
# Random selection function
def random_selection(sentences, sen_len, limit = 5):

    if sen_len == 0:
        # Error message prompt
        st.error("I currently cant fine any sentences. Please upload a text file with sentences, or use the inbuilt list.")
        
        # terminate the entire program
        st.stop()
        
    else:
        select_sent = sentences[random.randint(0, len(sentences))]

        all_words = select_sent.split()
        if len(all_words) < 6:      # this is to ensure that the sentence has more than 6 words, if not, it will return None
            return None
        else:
            select_words = random.sample(all_words, k=min(len(all_words), limit))   # limit = number of sentences to select
            return select_sent, select_words
    
# possible tags
tags = ['Person', 'Location', 'Date', 'Number', 'Org', 'Other']




## ------------------------------------------------------------------------------------------------------------

# main
def main():
    st.title("NER Tagging Tool")

    # add a border around the upload section
    with sidebar:
        upload_container = st.container()
        with upload_container:

            # add a checkbox to use an inbuilt list
            use_builtin_list = st.sidebar.checkbox("Use Inbuilt List")

            # if checkbox is checked, use inbuilt list, also handles sentences list object
            if use_builtin_list:
                sentences = sw_sentences
                sen_len = len(sentences)

                st.markdown("Using inbuilt sentence list")
            
            else:                
                # ask user to upload a file
                file = st.file_uploader("Choose a file", type=["txt"])
                if is_text_file:
                    # convert file to list of sentences
                    sentences = read_file(file)
                    sen_len = len(sentences)
                else:
                    st.error("File is not a text file. Please upload a text file.")
                st.markdown("Using uploaded file sentence list")

            # clear file button
            if st.button("Clear", type='primary', help="Clear the file"):
                file = None


    # add a border around the print section
    print_container = st.container()
    with print_container:
        st.write(f"Number of sentences: {len(sentences)}")
        st.markdown("----")

    # tagging container
    tagging_container = st.container()

    # add a border around the tagging section
    with tagging_container:
        sent, tokens = random_selection(sentences, sen_len)
        st.write(sent)
        st.markdown("----")

        curr_tag = {}

        # loop to tag the sentences
        for i, token in enumerate(tokens):
            st.write("Select a tag for the token:")
            tag = st.radio(token, tags, key = i)
            st.write(f"Token: {token}, Tag: {tag}")

if __name__ == "__main__":
    main()