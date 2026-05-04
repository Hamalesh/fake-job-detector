from flask import Flask, request, render_template
from preprocess import preprocess_text

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        text = request.form.get("text", "")

        if not text.strip():
            return "Please enter some text"

        processed = preprocess_text(text)

        # Dummy output (replace with your ML model)
        result = "Fake Job" if "fake" in processed else "Real Job"

        return render_template("index.html", prediction=result)

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)
