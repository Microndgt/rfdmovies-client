import sys
import logging

from rfdmovie.config import get_config

logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, get_config("logging.level", "DEBUG").upper(), "DEBUG"))
handler = logging.StreamHandler(stream=sys.stderr)
handler.setFormatter(logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s %(message)s"))
logger.addHandler(handler)
