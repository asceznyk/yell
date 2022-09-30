from flask import Flask, Blueprint, render_template

bp = Blueprint('app', __name__, url_prefix='/')

@bp.route("/")
def main_page():
    return render_template('main.html')



