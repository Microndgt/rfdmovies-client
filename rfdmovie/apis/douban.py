import re
import time
from urllib import parse
from datetime import datetime
from bs4 import BeautifulSoup as bs

from rfdmovie.config import get_config
from rfdmovie.logger import logger
from rfdmovie.cache.movie import MovieCache
from . import BaseAPI, HtmlDownloader, HtmlParser, Search


class DoubanAPI(BaseAPI):
    @classmethod
    def read(cls, key_word, num=5):
        """
        从豆瓣读取电影信息，并且更新数据库缓存
        :param key_word:
        :param num:
        :return: list(dict)
        """
        return cls.read_all(key_word)[:num]

    @classmethod
    def read_all(cls, key_word):
        """

        :param key_word:
        :return: list(dict)
        """
        search = DoubanSearch()
        res = search.search(key_word)
        MovieCache.write_all(res)
        return res


class DoubanParser(HtmlParser):

    def parse_search_results(self, html):
        """
        返回搜索的结果解析
        :param html:
        :return:
        """
        soup = bs(html, "html5lib")
        movie_urls = []
        movie_links = soup.find_all("a", class_="cover-link")
        for movie_link in movie_links:
            if movie_link.img:
                movie_info = (movie_link.img['alt'], movie_link['href'])
                movie_urls.append(movie_info)
        return movie_urls

    def parse_pages(self, html):
        """
        解析是否多页
        :param html:
        :return:
        """
        soup = bs(html, "html5lib")
        pages = int(soup.find('span', class_="thispage")['data-total-page'])
        return pages

    def parse_page_results(self, html):
        """
        返回具体页面解析
        :param html:
        :return:
        """
        soup = bs(html, "html5lib")

        movie_data = {}

        content = soup.find('div', id='content')

        name_and_year = [item.get_text() for item in content.find("h1").find_all("span")]
        name, year = name_and_year if len(name_and_year) == 2 else (name_and_year[0], "")

        movie_data["name"] = name.strip()
        year = year.strip("()")

        if year and year not in {"？", "?"}:
            year = year.replace("?", "0")
            try:
                release_year = re.search(r"(\d{4})", year).group(1)
            except:
                print(year)
                movie_data["release_time"] = "1900-01-01"
            else:
                release_time = datetime.strptime(release_year, "%Y").strftime("%Y-%m-%d")
                movie_data["release_time"] = release_time
        else:
            movie_data["release_time"] = "1900-01-01"

        content_right = soup.find("div", class_="rating_wrap clearbox")
        if content_right:
            rate = content_right.find("strong", class_="ll rating_num").get_text()
            movie_data["rate"] = float(rate) if rate else 5.0

            rating_people = content_right.find("a", class_="rating_people")
            movie_data["rate_num"] = int(rating_people.find("span").get_text()) if rating_people else 500
        else:
            movie_data["rate"] = 5.0
            movie_data["rate_num"] = 500

        content_left = soup.find("div", class_="subject clearfix")
        info = content_left.find("div", id="info").get_text()
        info_dict = dict([line.strip().split(":", 1)
                          for line in info.strip().split("\n") if line.strip().find(":") > 0])

        movie_data["types"] = [item.strip() for item in info_dict.get("类型", "").split('/') if item]
        directors = [item.strip() for item in info_dict.get("导演", "").split('/') if item]
        movie_data["director"] = directors and directors[0].strip() or ''
        movie_data["actors"] = [item.strip() for item in info_dict.get("主演", "").split('/') if item]
        movie_data["countries"] = [item.strip() for item in info_dict.get("制片国家/地区", "").split('/') if item]
        movie_data["languages"] = [item.strip() for item in info_dict.get("语言", "").split('/') if item]

        rating_pers = soup.find_all("span", class_="rating_per")
        if rating_pers:
            orders = ('grade_five', "grade_four", "grade_three", "grade_two", "grade_one")
            for key, rating_per in zip(orders, rating_pers):
                movie_data[key] = round(float(re.search(r"([\d|\.]+)", rating_per.get_text()).group(1)) / 100, 4)
        else:
            movie_data["grade_five"] = movie_data["grade_four"] = movie_data["grade_three"] =\
                movie_data["grade_two"] = movie_data["grade_one"] = 0.25
        return movie_data


class DoubanDownloader(HtmlDownloader):
    pass


class DoubanSearch(Search):
    def __init__(self):
        self.search_url = get_config("douban.search")
        self.downloader = DoubanDownloader()
        self.parser = DoubanParser()
        self.headers = {
            'Host': 'movie.douban.com',
            "Referer": "https://movie.douban.com/"
        }

    def _encode(self, name):
        raise NotImplementedError

    def search(self, name):
        name_code = parse.quote(name)
        search_url = self.search_url + name_code
        search_res = self.downloader.phjs_get(search_url)
        page_urls = self.parser.parse_search_results(search_res)

        res = []
        # TODO 获取多个页面的数据 目前只获取第一页
        for name, url in page_urls:
            time.sleep(1)
            logger.info("Getting douban movie: {} data".format(name))
            search_res = self.downloader.get(url, ext_headers=self.headers)
            movie_data = self.parser.parse_page_results(search_res)
            movie_data["douban_url"] = url
            res.append(movie_data)
        return res
