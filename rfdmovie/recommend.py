import numpy as np

from rfdmovie.models import Movie
from .logger import logger
from .cache.movie import MovieCache

# TODO 优化算法，使得 rate 和 rate_num 占的比重更大一些

items = "爱情 喜剧 动画 剧情 科幻 动作 悬疑 青春 犯罪 惊悚 恐怖 纪录片 战争 励志" \
        " 传记 真人秀 情色 冒险 搞笑 音乐 女性 魔幻 浪漫 历史 同性 运动 短片 歌舞 奇幻 脱口秀".split()


def movies_as_matrix(movies):
    matrix = []
    for movie in movies:
        array = [movie['id'], movie['rate'], movie['rate_num']]
        for item in items:
            if item in movie['types']:
                array.append(1)
            else:
                array.append(0)
        matrix.append(array)
    return matrix


def handle_movie_data(movie_data, sum_range):
    '''处理电影信息(嵌套列表),返回一个数组向量'''
    movie_data = movie_data[0]
    # rate
    movie_data[1] /= 10
    movie_data[2] /= sum_range
    data = list(map(float, movie_data[1:]))
    return np.array(data)


def trans_data(raw_data, sum_range):
    '''将数据库查询的数据转换为numpy矩阵'''
    data_len = len(raw_data)
    columns = len(raw_data[0]) - 1
    mats = np.zeros((data_len, columns))
    for index, data in enumerate(raw_data):
        data = list(data)
        # 数据归一化 rate sum
        data[2] = float(data[2]) / sum_range
        # rate
        data[1] = float(data[1]) / 10
        temp_data = [float(ele) for ele in data[1:]]
        mats[index, :] = temp_data
    return mats


def classify(inX, data_set, k=10):
    '''一个基于欧几里得距离算法的分类器'''
    data_set_size = data_set.shape[0]
    diff_mat = np.tile(inX, (data_set_size, 1)) - data_set
    sqDiffMat = diff_mat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    # 返回排序索引值
    sortedDistIndices = distances.argsort()
    return sortedDistIndices[:k]


def rate_sum_range(data):
    '''寻找最大和最少评分人数,对评分人数进行归一化处理'''
    max_sum = float(max(data))
    min_sum = float(min(data))
    return max_sum - min_sum


def recommend(name):
    base_movie = MovieCache.read(name, num=1)
    if not base_movie:
        return []
    # TODO 给出电影列表，让用户选择电影
    logger.info("您选择的电影是: {}".format(base_movie[0]['name']))
    remain_movies = MovieCache.read_by_filter(cond=(Movie.id != base_movie[0]['id']))
    movie_data = movies_as_matrix(base_movie)
    movies_data = movies_as_matrix(remain_movies)
    rate_sum_data = [movie['rate_num'] for movie in base_movie + remain_movies]
    # 归一化
    sum_range = rate_sum_range(rate_sum_data)
    inX = handle_movie_data(movie_data, sum_range)
    data_set = trans_data(movies_data, sum_range)
    indexes = classify(inX, data_set)
    recommend_moives = []
    for i in indexes:
        recommend_moives.append(movies_data[i])
    final_recommend = sorted(recommend_moives, key=lambda x: x[1] * x[2], reverse=True)
    recommends = []
    for raw_movie in final_recommend:
        movie = MovieCache.read_by_id(raw_movie[0])
        recommends.append(movie)
    return recommends
