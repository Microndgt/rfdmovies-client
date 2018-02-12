from rfdmovie.models import Download
from rfdmovie.db import db_session
from . import BaseCache


class DownloadCache(BaseCache):
    @classmethod
    def write(cls, download):
        db_download = Download(**download)
        db_session.add(db_download)
        db_session.commit()

    @classmethod
    def write_all(cls, downloads):
        for download in downloads:
            db_download = Download(**download)
            db_session.add(db_download)
        db_session.commit()

    @classmethod
    def read(cls, key_word, num=5):
        items = db_session.query(Download).filter(
            Download.name.like("%{}%".format(key_word))).order_by(Download.id.desc()).limit(num).all()
        return [item.to_dict() for item in items]
