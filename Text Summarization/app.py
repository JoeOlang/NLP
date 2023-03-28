text = """
There are broadly two types of extractive summarization tasks depending on what the summarization program focuses on. The first is generic summarization, which focuses on obtaining a generic summary or abstract of the collection (whether documents, or sets of images, or videos, news stories etc.). The second is query relevant summarization, sometimes called query-based summarization, which summarizes objects specific to a query. Summarization systems are able to create both query relevant text summaries and generic machine-generated summaries depending on what the user needs.
An example of a summarization problem is document summarization, which attempts to automatically produce an abstract from a given document. Sometimes one might be interested in generating a summary from a single source document, while others can use multiple source documents (for example, a cluster of articles on the same topic). This problem is called multi-document summarization. A related application is summarizing news articles. Imagine a system, which automatically pulls together news articles on a given topic (from the web), and concisely represents the latest news as a summary.
Image collection summarization is another application example of automatic summarization. It consists in selecting a representative set of images from a larger set of images.[3] A summary in this context is useful to show the most representative images of results in an image collection exploration system. Video summarization is a related domain, where the system automatically creates a trailer of a long video. This also has applications in consumer or personal videos, where one might want to skip the boring or repetitive actions. Similarly, in surveillance videos, one would want to extract important and suspicious activity, while ignoring all the boring and redundant frames captured.
"""

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list(STOP_WORDS)

nlp = spacy.load('en_core_web_sm')

text2 = "we should be given more materials for learning Get rid of assignments None i wish that we could start over learning it again Have one group assignment replace one lab exercise More time The practical lessons are a bit difficult to follow  That we could be offered more detailed information on the slide notes for revision purposes. It is hard to understand clearly on notes written almost in point form without details to explain the how of an event. more time Everything is good to me 1. I just wanna go back to school. None. Very content It has to many codes for someone to master continue teaching as it is  Regarding makeup cat the lec should consider choosing the highest for those redoing it it should be spaced oy because it is somehow quite difficult Leniency is marking juu enyewe an idea is better than none All seems well at the moment Extension of submission times for assignments everything about the subject is cool Extension of submission times for assignments I wish the concepts taught would not be too complicated Better explanation of codes when doing a demo more examples I wish it would be taught physically More group assignments. Individual feedback. null 1.To learn practically. I wish to gain greatly. the lec should move a bit slower  I have none So far so good. No wishes. To pass To pass  To pass in it none None More examples for illustration Real life projects that we can apply it  1.More engagement time. more code examples  Clearer questions to understand it boost the participation  to pass it None at the moment No wish cause everything is okay nothing much T b more texts  more code examples  its hard Stop using our free time  more explanation on practicals 1. MORE EXAMPLES More clear examples to be used. it is just fine that I could understand whatever is being tought, that subject is quite hard and complicated for the normal mind to understand. To have more time on practicals more practical examples  I have none. No comment.  None at the moment it never ends My wish is , if it possible for the unit to be added more hours for better understanding of the unit. None whatsoever None whatsoever It is all good  More practical examples some people have no idea what this unit really entails More contact time. That it would be a little easier I wish for more real life examples to enhance understanding More assignments,and appropriate feedback for each student. lesson is too long dont go too fast i dont know how to code im a slow learner"

doc = nlp(text)
doc2 = nlp(text2)

tokens = [token.text for token in doc]
print(tokens)

tokens2 = [token.text for token in doc2]

punctuation = punctuation + '\n'
punctuation

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
                
print(word_frequencies)

word_frequencies2 = {}
for word in doc2:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies2.keys():
                word_frequencies2[word.text] = 1
            else:
                word_frequencies2[word.text] += 1

max_frequency2 = max(word_frequencies2.values())
max_frequency2

for word in word_frequencies2.keys():
    word_frequencies2[word] = word_frequencies2[word]/max_frequency2

print(word_frequencies)

sentence_tokens2 = [sent for sent in doc2.sents]
print(sentence_tokens2)

sentence_scores2 = {}
for sent in sentence_tokens2:
    for word in sent:
        if word.text.lower() in word_frequencies2.keys():
            if sent not in sentence_scores2.keys():
                sentence_scores2[sent] = word_frequencies2[word.text.lower()]
            else:
                sentence_scores2[sent] += word_frequencies2[word.text.lower()]
                
sentence_scores2

from heapq import nlargest

select_length2 = int(len(sentence_tokens2)*0.3)
select_length2

summary2 = nlargest(select_length2, sentence_scores2, key = sentence_scores2.get)
summary2

final_summary2 = [word.text for word in summary2]
summary2 = ' '.join(final_summary2)

print(text2)

print(summary2)

len(text2)

len(summary2)

