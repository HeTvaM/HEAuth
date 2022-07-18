import sys
import logging
from logging import StreamHandler, Formatter
from patterns import MetaSingleton

class Logger(metaclass = MetaSingleton):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    
    handler = StreamHandler(stream=sys.stdout)
    handler.setFormatter(Formatter(fmt='[%(asctime)s: %(levelname)s] %(message)s'))
    
    logger.addHandler(handler)
    
    def log(self, data):
        self.logger.info(data)
    
    def log_exception(self, exception):
        self.logger.error(exception)