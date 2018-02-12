import random
import requests
from selenium import webdriver

USER_AGENTS = ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
               'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0',
               'Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0',
               ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) '
                'Chrome/19.0.1084.46 Safari/536.5'),
               ('Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.46'
                'Safari/536.5'),)


class BaseAPI:
    @classmethod
    def read(cls, key_word, num=5):
        """

        :param key_word:
        :param num:
        :return: list(dict)
        """
        raise NotImplementedError

    @classmethod
    def read_all(cls, key_word):
        """

        :param key_word:
        :return: list(dict)
        """
        raise NotImplementedError


class HtmlParser:
    def parse_search_results(self, html):
        """
        返回搜索的结果解析
        :param html:
        :return:
        """
        raise NotImplementedError

    def parse_pages(self, html):
        """
        解析是否多页
        :param html:
        :return:
        """
        raise NotImplementedError

    def parse_page_results(self, html):
        """
        返回具体页面解析
        :param html:
        :return:
        """
        raise NotImplementedError


class HtmlDownloader:
    def download(self, url, filename):
        """
        下载对应 url 的文件
        :param url:
        :param filename:
        :return:
        """
        pass

    def phjs_get(self, search_url):
        driver = webdriver.PhantomJS()
        driver.get(search_url)
        html = driver.page_source
        driver.close()
        return html

    def get(self, search_url, decoding="utf-8", ext_headers=None):
        headers = {'User-Agent': random.choice(USER_AGENTS)}
        if ext_headers:
            headers.update(ext_headers)
        req = requests.get(search_url, headers=headers)
        if req.status_code // 200 != 1:
            return
        return req.content.decode(decoding, 'ignore')


class Search:

    def _encode(self, name):
        raise NotImplementedError

    def search(self, name):
        raise NotImplementedError
