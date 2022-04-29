from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    message = "Hellow Friday am making revisoon"
    # return render_template('index.html')
    return render_template("index.html", message = message)
