import os
import urllib.request
from flask import Flask, render_template, request
#from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        f = request.get_json(force=True)
        f = urllib.request.urlopen(f['audio'])
        with open('./temp/audio.ogg', 'wb') as out:
            out.write(f.read())
        return 'audio sent successfully'
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

