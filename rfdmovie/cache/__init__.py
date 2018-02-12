"""
每次查询或者下载之后都会将所有出现的结果存储到数据库中
命令行工具按照 --cache 来决定是否使用数据库中的数据还是直接搜索

这里 cache 包定义了对 find 的电影信息，download 的电影信息 存储以及读取数据库的操作
对于 recommend 为实时计算，并不进行缓存操作

其实是对数据库中的电影信息进行 增改查
"""


class BaseCache:
    @classmethod
    def read(cls, key_word, num=5):
        """

        :param key_word:
        :param num:
        :return: list(dict)
        """
        raise NotImplementedError

    @classmethod
    def read_by_id(cls, movie_id):
        """

        :param movie_id:
        :return: dict
        """
        raise NotImplementedError

    @classmethod
    def read_all(cls, key_word):
        """

        :param key_word:
        :return: list(dict)
        """
        raise NotImplementedError

    @classmethod
    def write(cls, movie):
        raise NotImplementedError

    @classmethod
    def write_all(cls, movies):
        raise NotImplementedError

    @classmethod
    def update(cls, movie_id, movie):
        """
        更新某个movie的信息
        :param movie_id:
        :param movie: dict
        :return: dict
        """
        raise NotImplementedError
