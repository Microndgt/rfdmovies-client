"""
读取 data 目录下已经解析好的电影信息文件，存储到数据库
"""
import os
import re
from datetime import datetime
from rfdmovie.config import project_root
from rfdmovie.cache.movie import MovieCache

MOVIE_DATA_FILE = os.path.abspath(os.path.join(project_root, "./data/doubanmovie.txt"))


def read_file(file_path):
    movies = []
    for line in open(file_path, 'r'):
        movie_dict = parse_line(line)
        if movie_dict:
            movies.append(movie_dict)
    return movies


def parse_line(line):
    elements = line.split("\t")
    if len(elements) != 21:
        return {}
    print("movie: {}".format(elements[1]))
    res = {
        "douban_url": elements[0],
        "name": elements[1],
        "image_url": elements[3],
        "director": elements[4].strip(),
        "actors": [element.strip() for element in elements[6].split("/")],
        "types": [element.strip() for element in elements[7].split("/")],
        "countries": [element.strip() for element in elements[8].split("/")],
        "languages": [element.strip() for element in elements[9].split("/")],
        "keywords": [element.strip() for element in elements[14].split("/")],
        "rate": float(elements[18]) if elements[18] else 0,
        "rate_num": int(elements[19]) if elements[19] else 0,
    }

    if elements[2] and elements[2] not in {"？", "?"}:
        elements[2] = elements[2].replace("?", "0")
        try:
            release_year = re.search(r"(\d{4})", elements[2]).group(1)
        except:
            print(elements[2])
            res["release_time"] = "1900-01-01"
        else:
            release_time = datetime.strptime(release_year, "%Y").strftime("%Y-%m-%d"),
            res["release_time"] = release_time
    else:
        res["release_time"] = "1900-01-01"

    try:
        duration = int(re.search(r"(\d+)", elements[13]).group(1)) if elements[13] else 0
    except:
        print(elements[13])
        duration = 0
    res["duration"] = duration

    grades = elements[20].strip("\n").split(",")
    if grades[0]:
        res["grade_five"] = float(re.search(r"([\d|\.]+)", grades[0]).group(1)) / 100
        res["grade_four"] = float(re.search(r"([\d|\.]+)", grades[1]).group(1)) / 100
        res["grade_three"] = float(re.search(r"([\d|\.]+)", grades[2]).group(1)) / 100
        res["grade_two"] = float(re.search(r"([\d|\.]+)", grades[3]).group(1)) / 100
        res["grade_one"] = float(re.search(r"([\d|\.]+)", grades[4]).group(1)) / 100
    else:
        res["grade_five"] = res["grade_four"] = res["grade_three"] = res["grade_two"] = res["grade_one"] = 0
    return res


def main():
    movies = read_file(MOVIE_DATA_FILE)
    MovieCache().write_all(movies)


if __name__ == '__main__':
    main()
