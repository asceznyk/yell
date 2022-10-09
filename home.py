import os
import io
import speech_recognition as sr

from scipy.io import wavfile

from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_DIR"] = "temp"

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = sr.Recognizer()

        fp = os.path.join(app.config["UPLOAD_DIR"], 'sample.wav')
        f = open(fp, 'wb')
        f.write(request.data)
        f.close()

        r = wavfile.read(fp, 'rb')

        #with sr.AudioFile(fp) as source: print('blech!')

        #audio = model.listen(request.data)
        #text = model.recognize_google(audio)

        text = 'some crap'
        return {'msg':text, 'saved_path':fp}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

