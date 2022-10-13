import os
import io
import wave

import numpy as np
import speech_recognition as sr

from flask import Flask, render_template, request
from pydub import AudioSegment

app = Flask(__name__)
app.config["UPLOAD_DIR"] = "temp"

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = sr.Recognizer()
        
        text = "no audio"
        try:
            fp = os.path.join(app.config["UPLOAD_DIR"], 'audio_sample.webm') 
            
            fx = open(fp, 'wb')
            fx.write(request.data)
            fx.close()

            wavfp = fp.replace('webm', 'wav')

            webm = AudioSegment.from_file(fp, 'webm') 
            webm.export(wavfp, format='wav') 
            with sr.AudioFile(wavfp) as source:  
                sound = model.listen(source)
            text = model.recognize_google(sound)
        except Exception as e:
            text = f'error: {e}'

        return {'msg':text}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

