import os
import sys
import logging

logging.basicConfig(
    format='%(asctime)s #%(lineno)s %(levelname)s %(name)s :::  %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG,
    stream=sys.stdout,
)

logger = logging.getLogger(__name__)


class IlysAobaBot(object):
    def __init__(self, dialogue_model):
        self.model = dialogue_model
        self.history = []

    def predict(self, text):
        self.history.append(text)
        responses = self.model(self.history)
        self.history.append(responses[0])
        logger.info('\033[32m' + f'In : {text}' + '\033[0m')
        logger.info('\033[32m' + f'Out: {responses[0]}' + '\033[0m')
        return self.history
    
    def clear(self,):
        self.history = []
