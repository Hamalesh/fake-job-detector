from flask import Flask, request, render_template
import joblib
import numpy as np
import scipy.sparse
from preprocess import preprocess_text
import nltk
import nltk
nltk.data.path.append("/opt/render/nltk_data")


app = Flask(__name__)

model = joblib.load('Models/xgboost_model.pkl')
vectorizer = joblib.load('Models/tfidf_vectorizer.pkl')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['job_text']

    clean = preprocess_text(text)
    text_vec = vectorizer.transform([clean])

    meta = np.array([[0, 0, 0, len(text)]])
    X = scipy.sparse.hstack([text_vec, meta])

    prediction = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    if prediction == 1:
        result = f"Fake Job ❌ (Confidence: {round(prob*100,2)}%)"
    else:
        result = f"Legitimate Job ✅ (Confidence: {round((1-prob)*100,2)}%)"

    return render_template('index.html', result=result)   # 👈 INSIDE FUNCTION
import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
