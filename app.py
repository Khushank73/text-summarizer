from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the summarization pipeline
summarizer = pipeline('summarization')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    if request.method == 'POST':
        # Get the input text from the form
        text = request.form['text']
        min_length = int(request.form['min_length'])
        max_length = int(request.form['max_length'])

        # Generate the summary using the summarization pipeline
        summary = summarizer(text, max_length=120, min_length=30, do_sample=True)
        summary = summary[0]['summary_text']

        return render_template('result.html', text=text, summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
