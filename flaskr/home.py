from flask import Flask, Blueprint, Response, render_template
import pyaudio

bp = Blueprint('app', __name__, url_prefix='/')

@bp.route("/")
def main_page():
    return render_template('main.html')



