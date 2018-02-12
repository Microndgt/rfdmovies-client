from datetime import datetime


def generate_timestamp():
    utcnow = datetime.utcnow()
    epoch = datetime.utcfromtimestamp(0)
    delta = utcnow - epoch
    return int(delta.total_seconds())
