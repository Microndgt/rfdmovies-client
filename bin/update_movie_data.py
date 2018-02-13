"""
数据库中 rate 为 5 的电影 与 豆瓣电影 数据 同步
"""

from tqdm import tqdm
from rfdmovie.models import Movie
from rfdmovie.apis.douban import DoubanAPI
from rfdmovie.cache.movie import MovieCache


def get_update_movies():
    cond = (Movie.rate == 5) & (Movie.release_time < '2018-01-01')
    items = MovieCache.read_by_filter(cond)
    return [item['name'] for item in items]


def update(movie_name):
    DoubanAPI.read(movie_name, num=5)


def main():
    for movie_name in tqdm(get_update_movies()):
        update(movie_name)


if __name__ == '__main__':
    main()
