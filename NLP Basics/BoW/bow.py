import sklearn
from sklearn.feature_extraction.text import CountVectorizer


texts = ["This is a good child", "This was a bad child"]

v = CountVectorizer()

vectorizer = CountVectorizer(token_pattern=u"(?u)\\b\\w+\\b", min_df=1)
vectorizer.fit(texts)

# View how many words we have. '
print("Vocabulary Size: {}". format(len(vectorizer.vocabulary_)))

# Take note of the numbering as this is different from the article
print("Vocabulary Items: {}". format(vectorizer.vocabulary_))

bag_of_words = vectorizer.transform(texts)

print(bag_of_words)

print("BOW as an array: {}". format(bag_of_words.toarray()))

