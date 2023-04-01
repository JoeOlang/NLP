import random
import json

# ----------------------------------------------------------------------------------- #
# 1. Load the data  #
data = 'Data/RFI April - November 2022 titles - cleaned.txt'
with open(data, 'r') as f:
    sentences = f.read().split('\n')

# ----------------------------------------------------------------------------------- #
# Random selection function
def random_selection():
    select_sent = sentences[random.randint(0, len(sentences))]

    all_words = select_sent.split()
    if len(all_words) < 6:      # this is to ensure that the sentence has more than 6 words, if not, it will return None
        return None
    else:
        select_words = random.sample(all_words, k=min(len(all_words), 5))
        return select_sent, select_words
    
# ----------------------------------------------------------------------------------- #
# possible tags
tags = ['Person', 'Location', 'Date', 'Number', 'Org', 'Other']


# ----------------------------------------------------------------------------------- #

number_of_its = int(input('How many sentences do you want to tag? '))

# initialize the document tracker
doc_tracker = 1

# a loop to tag the sentences
for i in range(number_of_its):

    sample_sent, sample_toks = random_selection()

    all_tags = {}

    for token in sample_toks:
        print(sample_sent)
        print("-"*len(sample_sent))
        print(f"What tag should '{token}' have? Please choose from the following options: {tags}")
        tag = input().strip()
        while tag not in tags:
            print(f"Invalid tag. Please choose from the following options: {tags}")
            tag = input().strip()
        all_tags[token] = tag

    result = {}

    # add sentence to result
    result['sentence'] = sample_sent

    # add token_tags to result
    token_tags = []
    for token in sample_toks:
        token_tags.append({'token': token, 'tag': all_tags[token]})

    result['token_tags'] = token_tags

    print(result)
    print("*"*len(sample_sent))


    # save the result
    doc_name = "file" + str(doc_tracker) + ".json"
    with open(doc_name, 'w') as f:
        json.dump(result, f)

    print('Document saved as: ', doc_name)

    doc_tracker += 1

# ----------------------------------------------------------------------------------- #