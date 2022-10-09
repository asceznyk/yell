import os
import io
import speech_recognition as sr

#from scipy.io import wavfile
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = sr.Recognizer()

        f = open('./file.wav', 'wb')
        f.write(request.data)
        f.close()

        with sr.AudioFile('./file.wav') as source: print('blech!')

        #audio = model.listen(r.read())
        #text = model.recognize_google(audio)

        text = 'some crap'
        return {'msg':text}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

