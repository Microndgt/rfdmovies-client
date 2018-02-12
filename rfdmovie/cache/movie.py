from rfdmovie.models import Movie
from rfdmovie.db import db_session
from . import BaseCache


class MovieCache(BaseCache):
    @classmethod
    def write(cls, movie, update=True):
        if update:
            exist_movie = cls.read_by_douban_url(movie['douban_url'])
            if exist_movie:
                cls.update(exist_movie, movie)
                db_session.commit()
                return
        db_movie = Movie(**movie)
        db_session.add(db_movie)
        db_session.commit()

    @classmethod
    def write_all(cls, movies, update=True):
        for movie in movies:
            if update:
                exist_movie = cls.read_by_douban_url(movie['douban_url'])
                if exist_movie:
                    cls.update(exist_movie, movie)
                    continue

            db_movie = Movie(**movie)
            db_session.add(db_movie)
        db_session.commit()

    @classmethod
    def update(cls, exist_movie, movie):
        if movie['rate']:
            exist_movie['rate'] = movie['rate']
        if movie['rate_num']:
            exist_movie['rate_num'] = movie['rate_num']
        if movie['grade_five']:
            exist_movie['grade_five'] = movie['grade_five']
        if movie['grade_four']:
            exist_movie['grade_four'] = movie['grade_four']
        if movie['grade_three']:
            exist_movie['grade_three'] = movie['grade_three']
        if movie['grade_two']:
            exist_movie['grade_two'] = movie['grade_two']
        if movie['grade_one']:
            exist_movie['grade_one'] = movie['grade_one']
        db_session.query(Movie).filter(Movie.id == exist_movie['id']).update(exist_movie)

    @classmethod
    def read(cls, key_word, num=5):
        items = db_session.query(Movie).filter(
            Movie.name.like("%{}%".format(key_word)) | Movie.keywords.any(key_word)).\
            order_by(Movie.rate.desc()).limit(num).all()
        return [item.to_dict() for item in items]

    @classmethod
    def read_by_id(cls, movie_id):
        item = db_session.query(Movie).filter(Movie.id == movie_id).first()
        return item.to_dict() if item else {}

    @classmethod
    def read_by_douban_url(cls, douban_url):
        item = db_session.query(Movie).filter(Movie.douban_url == douban_url).first()
        return item.to_dict() if item else {}

    @classmethod
    def read_by_filter(cls, cond):
        # TODO support more filters
        items = db_session.query(Movie).filter(cond).all()
        return [item.to_dict() for item in items]
