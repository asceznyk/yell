import os
import io
import wave

import tempfile

import numpy as np
import speech_recognition as sr

from flask import Flask, render_template, request
from pydub import AudioSegment

app = Flask(__name__)

tempdir = "/tmp/"
for fname in os.listdir(tempdir): 
    if fname.startswith("yell_user_data_"): 
        app.config["UPLOAD_DIR"] = f"{tempdir}{fname}"
        break
else: 
    app.config["UPLOAD_DIR"] = tempfile.mkdtemp(prefix="yell_user_data_")

model = sr.Recognizer()

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST': 
        text = "no audio"
        try: 
            fp = os.path.join(app.config["UPLOAD_DIR"], f"audio_{request.files['audio_blob'].filename}") 
            request.files['audio_blob'].save(fp)
            wavfp = fp.replace('webm', 'wav')
            webm = AudioSegment.from_file(fp, 'webm') 
            webm.export(wavfp, format='wav') 
            with sr.AudioFile(wavfp) as source:  
                sound = model.listen(source)
            text = model.recognize_google(sound)
        except Exception as e:
            text = f'err_msg: {e}'

        return {'msg':text, 'ip': request.form['browser_id']}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0', port=os.environ.get('PORT', 5000))




