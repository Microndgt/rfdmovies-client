"""
每次查询或者下载之后都会将所有出现的结果存储到数据库中
命令行工具按照 --cache 来决定是否使用数据库中的数据还是直接搜索

这里 cache 包定义了对 find 的电影信息，download 的电影信息 存储以及读取数据库的操作
对于 recommend 为实时计算，并不进行缓存操作
"""


class BaseCache:
    def read(self, key_word, num=5):
        pass

    def read_all(self, key_word):
        pass

    def write(self):
        pass

    def write_all(self):
        pass
