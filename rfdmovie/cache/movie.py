from rfdmovie.models import Movie
from rfdmovie.db import db_session
from . import BaseCache


class MovieCache(BaseCache):
    def write(self, movie):
        db_movie = Movie(**movie)
        db_session.add(db_movie)
        db_session.commit()

    def write_all(self, movies):
        for movie in movies:
            db_movie = Movie(**movie)
            db_session.add(db_movie)
        db_session.commit()
