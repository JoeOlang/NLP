import pandas as pd
import spacy

# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

df = pd.read_csv('data.csv')

text = df['text'].tolist()
# print(text)

"""
text_file = open("data.txt", "w")
for element in text:
    text_file.write(element + "\n")
text_file.close()
"""


def print_ner(texts):
    doc = nlp(texts)
    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print("START")
        print(entity.text, entity.label_)
        print("STOP")


for i in text:
    print_ner(i)
