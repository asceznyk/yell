from flask import Flask, render_template

@bp.route("/")
def main_page():
    return render_template('main.html')



