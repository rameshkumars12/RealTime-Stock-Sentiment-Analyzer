import pandas as pd #For dataframe
import sys
from textblob import TextBlob #for sentiment analyze
from nltk.stem.snowball import SnowballStemmer #for removing stemmer words ex:ing
import re #for removing special char
import spacy
nlp = spacy.load('en_core_web_sm')

#Getting the dataset
def stocksentiment(data):
    df = pd.read_csv(data)

    #Looping through every single words
    all_sentences = []
    for word in df.Headlines:
        all_sentences.append(word)
    all_sentences

    #Splitting the words
    lines = list()
    for line in all_sentences:
        if type(line) == float:
            pass
        else:
            words = line.split()
            for w in words:
                lines.append(w)

    #Removing Punctuation
    lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
    lines2 = []

    for word in lines:
        if word != '':
            lines2.append(word)


    # The Snowball Stemmer requires that you pass a language parameter
    s_stemmer = SnowballStemmer(language='english')
    stem = []
    for word in lines2:
        stem.append(s_stemmer.stem(word))

    #Removing all Stop Words
    stem2 = []
    for word in stem:
        if word not in nlp.Defaults.stop_words:
            stem2.append(word)
    stem2

    #Joining the words to perform sentiment analyze
    stem3 = " ".join(stem2)
    stocksentiment.score = TextBlob(stem3).sentiment.polarity
    print(stocksentiment.score)

    if stocksentiment.score < 0:
        return "Negative"
    elif stocksentiment.score == 0:
        return "Neutral"
    else:
        return "Positive"


if __name__ == "__main__":
    stocksentiment(sys.argv[1])
