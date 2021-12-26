# Swahili Word Embedding Vectors

![](https://github.com/JoeOlang/NLP/blob/main/Swahili/Swahili%20Word%20Embedding%20Word2Vec%20-%20Model/media/embedings.gif)

A demo on traning word embedings which can be used as features in place of Tf-Idf &/ Count Vectorizer features. 
This technique maps words to real number vectors, at the same time capturing context of the text. If two words have similar meaning they will lie close to each other in a vector space. 
For this particular project the data used was in Swahili language and obtained from:

* Training Text Data:
* Common Swahili Stopwords:

Given the size of the dataset, the amount of learning done is not sufficient i.e. some words which should exhibit similar contnext sometimes have vectors values that are not close to each other. Training with more data can be a fix for this since using NLP task of this nature requre loads of data.

The next step is thefore to scrap more data and try to see if there is any significant improvements.

Feel free to share suggestions, thank you.

Some of the main libraries used are:
| Lib | Ref |
| ------ | ------ |
| pandas | [https://pandas.pydata.org/]|
| gensim | [https://pypi.org/project/gensim/]|
| nltk | [https://www.nltk.org/]|



## License
MIT
