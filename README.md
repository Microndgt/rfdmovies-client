rfdmovies-client
================

```
                                        ____                                              
            .--.,        ,---,         ,'  , `.                         ,--,               
  __  ,-. ,--.'  \     ,---.'|      ,-+-,.' _ |    ,---.              ,--.'|               
,' ,'/ /| |  | /\/     |   | :   ,-+-. ;   , ||   '   ,'\       .---. |  |,                
'  | |' | :  : :       |   | |  ,--.'|'   |  ||  /   /   |    /.  ./| `--'_        ,---.   
|  |   ,' :  | |-,   ,--.__| | |   |  ,', |  |, .   ; ,. :  .-' . ' | ,' ,'|      /     \  
'  :  /   |  : :/|  /   ,'   | |   | /  | |--'  '   | |: : /___/ \: | '  | |     /    /  | 
|  | '    |  |  .' .   '  /  | |   : |  | ,     '   | .; : .   \  ' . |  | :    .    ' / | 
;  : |    '  : '   '   ; |:  | |   : |  |/      |   :    |  \   \   ' '  : |__  '   ;   /| 
|  , ;    |  | |   |   | '/  ' |   | |`-'        \   \  /    \   \    |  | '.'| '   |  / | 
 ---'     |  : \   |   :    :| |   ;/             `----'      \   \ | ;  :    ; |   :    | 
          |  |,'    \   \  /   '---'                           '---"  |  ,   /   \   \  /  
          `--'       `----'                                            ---`-'     `----' 
            
Recommend && Find && Download Movie Cli

version 0.1.3
```

instant recommending or finding or downloading movies via the command line
--------------------------------------------------------------------------

Do you find it difficult to find an interesting movie to watch? Do you find yourself constantly Baidu for
which movie to watch? Or where to download?

Using this application, you will get the movie and information you are truly interested with. And furthermore, you will get the download links if there exists.

`rfdmovies` will find a movie info like this, `rfdmovies -f 冰与火之歌`

`rfdmovies` will recommend a movie base on movie name you provide, `rfdmovies -r 冰与火之歌`

`rfdmovies` will give you a movie downloading link like this, `rfdmovies -d 冰与火之歌`

Installation
------------

`pip install rfdmovies-client`

or

`pip install git+https://github.com/Microndgt/rfdmovies-client.git`

or

`python setup.py install`

load data
---

首先创建数据库并且更新到最新版本

```shell
bin/db_init.sh
bin/db_upgrade.sh
```

接下来运行下面两个命令其中一个即可将目前所有的电影数据导入数据库:

1. `psql -d rfdmovie -U postgres -p 35332 -f data/rfdmovie.sql`
2. `python -m bin.read_raw_movie_data`

目前共有47862条电影数据

Usage
-----

```
usage: rfdmovies.py [-h] [-r] [-f] [-d] [-p POS] [-a] [-l] [-c] [-n NUM_MOVIES] [-C] [-v] MOVIE [MOVIE ...]

instant coding answers via the command line

positional arguments:
  MOVIE                 the movie names you want to rfd

optional arguments:
  -h, --help            show this help message and exit
  -r, --recommend       recommend some new movies base on the movie name you provide
  -f, --find            find the movie info you provide
  -d, --download        display the download link for movie name you provide
  -p POS, --pos POS     select movie in specified position (default: 1)
  -a, --all             display the movie info and recommend results and download url
  -l, --link            display the movie info link or download link
  -c, --color           enable colorized output
  -n NUM_MOVIES, --num-movies NUM_MOVIES
                        number of movies to return, default is 5
  -C, --cache           using the cache
  -v, --version         displays the current version of rfdmovies
```

- 读取电影信息

    - `python -m rfdmovie -f -m "宝贝" -C` 使用cache数据
    - `python -m rfdmovie -f -m "宝贝" -C -c` 加上颜色输出
    
    ```
    +-----------------------------------------------+------+----------+------------------+---------------------------------------------+----------------------------------+--------------------------------------------+
    |                      name                     | rate | rate_num |    countries     |                   director                  |              types               |                 douban_url                 |
    +-----------------------------------------------+------+----------+------------------+---------------------------------------------+----------------------------------+--------------------------------------------+
    |    大自然的神奇宝贝 Nature's Miracle Babies   | 9.4  |   152    |     ['英国']     |                Annie Heather                |            ['纪录片']            | https://movie.douban.com/subject/11610536/ |
    |            宠物宝贝环游记 Pet Pals            | 9.3  |    50    |    ['意大利']    |                                             | ['喜剧', '动画', '儿童', '冒险'] | https://movie.douban.com/subject/20451503/ |
    | 数码宝贝：滚球兽的诞生 デジモンアドベンチャー | 8.9  |   1561   | ['日本', '日本'] |                    细田守                   |     ['动作', '动画', '冒险']     | https://movie.douban.com/subject/1303927/  |
    |         疯狂兔宝贝 The Bugs Bunny Show        | 8.9  |   226    |     ['美国']     | 查克·琼斯 / 弗里兹·弗里伦 / Robert McKimson |             ['动画']             | https://movie.douban.com/subject/3621340/  |
    |                阳光宝贝 Bébé(s)               | 8.8  |   3873   |     ['法国']     |                Thomas Balmès                |            ['纪录片']            | https://movie.douban.com/subject/3268358/  |
    +-----------------------------------------------+------+----------+------------------+---------------------------------------------+----------------------------------+--------------------------------------------+
    ```

- 电影下载链接

    - `python -m rfdmovie -d -m "宝贝" -C -c` 从本地数据库获取
    - `python -m rfdmovie -d -m "冰与火之歌" -c` 线上搜索

- 推荐

    - `python -m rfdmovie -r -m "黑客帝国" -C -c`

Author
------

- SkyRover([@Microndgt](http://skyrover.me))

Note
----

- Works with Python3

Using
---

- [xart](https://github.com/xlzd/xart) - generating art ASCII texts
- [prettytable](https://github.com/vishvananda/prettytable) - generate pretty table

History
===

- 0.1.3: 支持 电影天堂 搜索电影下载链接啦 `python -m rfdmovie -d -m "冰与火之歌" -c`
- 0.1.2: 支持 recommend，可以推荐电影啦 `python -m rfdmovie -r -m "黑客帝国" -C -c`
- 0.1.1: 支持 download 查询 cache 数据库操作 `python -m rfdmovie -d -m "宝贝" -C -c`
- 0.1.0: 导入原始数据，支持 find 查询 cache 数据库操作  `python -m rfdmovie -f -m "宝贝" -C -c`
