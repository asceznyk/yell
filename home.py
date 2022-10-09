import os
import speech_recognition as sr
from flask import Flask, render_template, request

app = Flask(__name__)
model = sr.Recognizer()

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        audio = request.files.get('audio')
        text = model.recognize_google(audio)
        return {'msg':'audio sent successfully'}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

