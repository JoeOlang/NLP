import pickle
from sentence_transformers import SentenceTransformer


# load numpy arrays from pickle file
with open('titles_np.pkl', 'rb') as f:
    titles = pickle.load(f)

with open('embeddings_np.pkl', 'rb') as f:
    embeddings = pickle.load(f)

# load the model
# model = pickle.load(open('model.sav' , 'rb'))

model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')
xq = model.encode('How to get started with Python?')

# load the index from disk
index = pickle.load(open('index.sav' , 'rb'))

D, I = index.search(xq, 5)
for i in I:
    print(titles[i])


""" def get_similar_documents(query, index, model, titles, k=5):
    xq = model.encode([query])
    D, I = index.search(xq, k)
    for i in I:
        print(titles[i])

get_similar_documents('What is the best way to learn Python?', index, model, titles) """