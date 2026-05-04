import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
STOPWORDS = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = nltk.word_tokenize(text)

    processed_words = []
    for word in words:
        if word not in STOPWORDS:
            processed_words.append(lemmatizer.lemmatize(word))

    return " ".join(processed_words)
