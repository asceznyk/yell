import os
import io
import wave

import numpy as np
import speech_recognition as sr

from scipy.io import wavfile

from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_DIR"] = "temp"

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = sr.Recognizer()
        
        text = "no audio"
        audio = request.files['audiof']

        if audio.filename.endswith('.wav'):
            try:
                fp = os.path.join(app.config["UPLOAD_DIR"], audio.filename) 
                audio.save(fp)

                #f = open(fp, 'wb')
                #f.write(request.data)
                #f.close()
         
                with sr.AudioFile(fp) as source:  
                    sound = model.listen(source)
                text = model.recognize_google(sound)
            except Exception as e:
                text = f'error: {e}'

        return {'msg':text}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

