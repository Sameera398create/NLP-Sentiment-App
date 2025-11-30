from flask import Flask, render_template, request
from sentiment.analyze import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_text = request.form.get("user_text", "").strip()
        if user_text:
            result = analyze_sentiment(user_text)
            result["text"] = user_text
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
