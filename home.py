import os
import io
import speech_recognition as sr

from werkzeug.wrappers import Request, Response
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["UPLOAD_DIR"] = "temp"

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        model = sr.Recognizer()

        f = open(os.path.join(app.config["UPLOAD_DIR"], 'sample.wav'), 'wb')
        f.write(request.data)
        f.close()

        #with sr.AudioFile('./file.wav') as source: print('blech!')

        #audio = model.listen(request.data)
        #text = model.recognize_google(audio)

        text = 'some crap'
        return {'msg':text, 'saved_path':os.path.join(app.config["UPLOAD_DIR"], 'sample.wav')}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

