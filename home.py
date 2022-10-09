import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        audio = request.files.get('audio')
        with open('./audio.wav', 'wb') as out:
            out.write(audio.read())
        return {'msg':'audio sent successfully'}
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

