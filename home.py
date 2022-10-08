import os
from flask import Flask, render_template, request
#from werkzeug import secure_filename

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        f = request['url']
        #f.save('./temp/audio.ogg')
        return f
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))

