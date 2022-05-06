from app.models import Review,User
from app import db

def setUp(self):
    self.user_James = User(username = 'Reuben',password = 'reubyreuby', email = 'reuby@ke.com')
    self.new_review = Review(movie_id=12345,movie_title='Review for movies',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",movie_review='This movie is the best thing since sliced bread',user = self.user_James )
    
  # clearing the  database after running each text      
def tearDown(self):
    Review.query.delete()
    User.query.delete()
#saving the data to the database 
def test_save_review(self):
    self.new_review.save_review()
    self.assertTrue(len(Review.query.all())>0)
    
# class method that we pass in the id of a movie and get a response which is a review for that movie.


def test_get_review_by_id(self):

    self.new_review.save_review()
    got_reviews = Review.get_reviews(12345)
    self.assertTrue(len(got_reviews) == 1)