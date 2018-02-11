rfdmovies-client
================

version
---

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

version 0.1
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
  -C, --clear-cache     clear the cache
  -v, --version         displays the current version of rfdmovies
```

Author
------

- SkyRover([@Microndgt](http://skyrover.me))

Note
----

- Works with Python3

Using
---

- [xart](https://github.com/xlzd/xart) - generating art ASCII texts