from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import sessionmaker

from rfdmovie.config import get_config

dsn_url = URL(drivername='postgresql', host=get_config("rfdmovie.postgresql.host"),
              port=get_config("rfdmovie.postgresql.port"),
              username=get_config("rfdmovie.postgresql.user"),
              password=get_config("rfdmovie.postgresql.password"),
              database=get_config("rfdmovie.postgresql.db_name"))

engine = create_engine(dsn_url, echo=get_config("rfdmovie.sqlalchemy.echo", False))
DBSession = sessionmaker(engine)  # pylint: disable=invalid-name
db_session = DBSession()
