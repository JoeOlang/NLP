import streamlit as st
from streamlit import sidebar
import io

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

# main app code
def main():
    st.title("Upload a Text File")

    # add a border around the upload section
    with sidebar:
        upload_container = st.container()
        with upload_container:

            # add a checkbox to use an inbuilt list
            use_builtin_list = st.sidebar.checkbox("Use Inbuilt List")

            # if checkbox is checked, use inbuilt list, also handles sentences list object
            if use_builtin_list:
                sentences = [
                    "This is the first sentence.",
                    "This is the second sentence.",
                    "This is the third sentence.",
                ]

                st.markdown("Using inbuilt sentence list")
            
            else:                
                # ask user to upload a file
                file = st.file_uploader("Choose a file", type=["txt"])
                if is_text_file:
                    # convert file to list of sentences
                    sentences = read_file(file)
                else:
                    st.error("File is not a text file. Please upload a text file.")
                st.markdown("Using uploaded file sentence list")

            # clear file button
            if st.button("Clear", type='primary', help="Clear the file", use_container_width=1):
                file = None


    # add a border around the print section
    print_container = st.container()
    with print_container:
        st.write(f"Number of sentences: {len(sentences)}")


if __name__ == "__main__":
    main()