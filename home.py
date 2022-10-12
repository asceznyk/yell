import os
import io
import wave

import numpy as np
import speech_recognition as sr

from scipy.io import wavfile

#from werkzeug import secure_filename 
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_DIR"] = "temp"

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        #model = sr.Recognizer()
        
        text = ".."
        fp = "path/to/something"
        #audio = request.files['audiof']
        #fp = os.path.join(app.config["UPLOAD_DIR"], audio.filename) 
        #audio.save(fp)

        #wave.open(fp, 'r')

        rb = wavfile.read('sample.wav')

        #f = open(fp, 'wb')
        #f.write(request.data)
        #f.close()
 
        #with sr.AudioFile(audio) as source: 
            #print('blech!')
            #sound = model.listen(source)
        #text = model.recognize_google(audio)

        return {'msg':text, 'saved_path':fp}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

