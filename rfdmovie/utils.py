from datetime import datetime


def generate_timestamp():
    utcnow = datetime.utcnow()
    epoch = datetime.utcfromtimestamp(0)
    delta = utcnow - epoch
    return int(delta.total_seconds())


def colored(color, text):
    '''shell下的颜色处理'''
    table = {
        'red': '\033[91m',
        'green': '\033[92m',
        # no color
        'nc': '\033[0m'
    }
    cv = table.get(color)
    nc = table.get('nc')
    return ''.join([cv, text, nc])
