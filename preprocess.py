print("FILE RUNNING")

import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Safe download (only if missing)
def safe_nltk_download():
    try:
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

safe_nltk_download()

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

def combine_fields(row):
    fields = [
        str(row.get('title', '')),
        str(row.get('company_profile', '')),
        str(row.get('description', '')),
        str(row.get('requirements', '')),
        str(row.get('benefits', ''))
    ]
    return " ".join(fields)
