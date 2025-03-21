# 日志记录
import logging
import os


class Logger:
    def __init__(self):
        filename = os.path.join(os.path.dirname(__file__), 'log.txt')
        logging.basicConfig(level=logging.ERROR, filename=filename, filemode='a', format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        self.logger = logging.getLogger()

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)