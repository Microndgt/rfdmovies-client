import argparse

from .logger import logger


desc = "Recommend && Find && Download Movie cli"
version_info = """
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
"""


def rfd_movie(movie_name, page_size=5, pos=0, output='./', color=True, action="find"):
    pass


def clear_cache():
    pass


def main():
    parse = argparse.ArgumentParser(description=desc)
    parseGroup = parse.add_argument_group()
    parseGroup.add_argument("-f", "--find", action="store_true", help="search mode")
    parseGroup.add_argument("-d", "--download", action="store_true", help="download mode")
    parseGroup.add_argument("-r", "--recommend", action="store_true", help="recommend mode")
    parse.add_argument("-v", "--version", action="store_true", help="print product version")
    parse.add_argument("-n", "--num", type=int, default=5, help="number of movies to return, default is 5")
    parse.add_argument("-p", "--pos", type=int, default=0, help="position for movie list to select")
    parse.add_argument("-o", "--output", type=str, default="./", help="path to output your movie")
    parse.add_argument("-g", "--page", type=int, default=1, help="the page you want to change")
    parse.add_argument("-c", "--color", action="store_true", help="enable colorized output")
    parse.add_argument("-C", "--clear", action="store_true", help="clear the cache")
    parse.add_argument("-m", "--movie", type=str, help="the movie names you want to rfd")
    args = parse.parse_args()

    if args.clear:
        clear_cache()

    if args.version:
        print(version_info)

    if args.find:
        logger.info("find MovieName: " + args.movie)
        rfd_movie(args.movie, args.num, args.pos, args.output, args.color, action="find")
    elif args.download:
        logger.info("download MovieName: " + args.movie)
        rfd_movie(args.movie, args.num, args.pos, args.output, args.color, action="download")
    elif args.recommend:
        logger.info("recommend MovieName: " + args.movie)
        rfd_movie(args.movie, args.num, args.pos, args.output, args.color, action="recommend")


if __name__ == "__main__":
    main()
