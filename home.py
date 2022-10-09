import os
import io
import speech_recognition as sr
from flask import Flask, render_template, request

app = Flask(__name__)
model = sr.Recognizer()

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        f = request.files.get('audio')
        
        file_obj = io.BytesIO()  
        file_obj.write(f.read()) 
        file_obj.seek(0)
        
        mic = sr.AudioFile(file_obj)
        with mic as source: audio = model.listen(source)
        #text = model.recognize_google(audio)

        text = 'some crap'
        return {'msg':text}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

