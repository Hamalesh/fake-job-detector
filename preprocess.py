print("FILE RUNNING")

import nltk
import string
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
def get_stopwords():
    try:
        from nltk.corpus import stopwords
        return set(stopwords.words('english'))
    except:
        return set()
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = nltk.word_tokenize(text)

    processed_words = []
    for word in words:
        if word not in stop_words():
            processed_words.append(lemmatizer.lemmatize(word))

    return " ".join(processed_words)

if __name__ == "__main__":
    sample = "Fake job offer high salary no experience"
    print(preprocess_text(sample))
def combine_fields(row):
    fields = [
        str(row.get('title', '')),
        str(row.get('company_profile', '')),
        str(row.get('description', '')),
        str(row.get('requirements', '')),
        str(row.get('benefits', ''))
    ]
    return " ".join(fields)
