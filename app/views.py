from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    """
    View root page function that returns the index page and its data
    """
    title = "welcome to my movie watchlist"
    message = "Hellow Friday am making revision"
    # return render_template('index.html')
    return render_template("index.html",title = title, message = message)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):

    '''
    View movie page function that returns the movie details page and its data
    '''
    # title = "my id"
    return render_template('movie.html', id = movie_id)