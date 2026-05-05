from flask import Flask, render_template, request
from summarizer import summarize

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    summary = ""
    if request.method == 'POST':
        text = request.form['text']
        summary = summarize(text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)