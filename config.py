import inspect
import os
import logging

from logging import FileHandler
from logging import Formatter
# https://docs.python.org/3.1/library/logging.html
LOG_FORMAT = (
            "%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d")
LOG_LEVEL = logging.DEBUG

# messaging logger
MESSAGING_LOG_FILE = "test.log"

logger = logging.getLogger("automation")
logger.setLevel(LOG_LEVEL)
logger_file_handler = FileHandler(MESSAGING_LOG_FILE)
logger_file_handler.setLevel(LOG_LEVEL)
logger_file_handler.setFormatter(Formatter(LOG_FORMAT))
logger.addHandler(logger_file_handler)

class GetDir(object):
    # ROOT_DIR = os.path.dirname(__file__)
    @property
    def ROOTDIR(self):
        return os.path.dirname(__file__)
    @property
    def REPORTDIR(self):
        return os.path.dirname(__file__)+'/Reports'
    @property
    def SCREENSHOTDIR(self):
        return os.path.dirname(__file__) + '/Screenshots'
