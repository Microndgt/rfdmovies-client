from sqlalchemy import ARRAY
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, BigInteger, Float, Date, Text

from rfdmovie.db import BaseModel
from rfdmovie.utils import generate_timestamp


class Movie(BaseModel):
    __tablename__ = 'movie'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    release_time = Column(Date)   # "1999-09-09"
    rate = Column(Float)
    rate_num = Column(BigInteger)
    desc = Column(Text)
    countries = Column(ARRAY(String))
    image_url = Column(String)
    types = Column(ARRAY(String))
    director = Column(String)
    actors = Column(ARRAY(String))
    douban_url = Column(String)
    keywords = Column(ARRAY(String))
    comments = Column(ARRAY(String))
    languages = Column(ARRAY(String))
    duration = Column(Integer)
    grade_five = Column(Float, default=0)
    grade_four = Column(Float, default=0)
    grade_three = Column(Float, default=0)
    grade_two = Column(Float, default=0)
    grade_one = Column(Float, default=0)
    created_utc = Column(Integer, default=generate_timestamp)
    updated_utc = Column(Integer, default=generate_timestamp, onupdate=generate_timestamp)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "release_time": self.release_time,
            "rate": self.rate,
            "rate_num": self.rate_num,
            "desc": self.desc,
            "countries": self.countries,
            "image_url": self.image_url,
            "types": self.types,
            "director": self.director,
            "actors": self.actors,
            "douban_url": self.douban_url,
            "keywords": self.keywords,
            "comments": self.comments,
            "languages": self.languages,
            "duration": self.duration,
            "grade_five": self.grade_five,
            "grade_four": self.grade_four,
            "grade_three": self.grade_three,
            "grade_two": self.grade_two,
            "grade_one": self.grade_one,
            "created_utc": self.created_utc,
            "updated_utc": self.updated_utc
        }


class Download(BaseModel):
    __tablename__ = 'download'
