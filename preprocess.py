print("FILE RUNNING")

import nltk
nltk.data.path.append("/opt/render/nltk_data")
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = nltk.word_tokenize(text)

    processed_words = []
    for word in words:
        if word not in stop_words:
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
