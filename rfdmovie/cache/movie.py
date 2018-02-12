from rfdmovie.models import Movie
from rfdmovie.db import db_session
from . import BaseCache


class MovieCache(BaseCache):
    @classmethod
    def write(cls, movie):
        db_movie = Movie(**movie)
        db_session.add(db_movie)
        db_session.commit()

    @classmethod
    def write_all(cls, movies):
        for movie in movies:
            db_movie = Movie(**movie)
            db_session.add(db_movie)
        db_session.commit()

    @classmethod
    def read(cls, key_word, num=5):
        items = db_session.query(Movie).filter(
            Movie.name.like("%{}%".format(key_word)) | Movie.keywords.any(key_word)).\
            order_by(Movie.rate.desc()).limit(num).all()
        return [item.to_dict() for item in items]
