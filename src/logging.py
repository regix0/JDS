'''
log.py implementation

    Functions:

    - take_log()
'''

import logging
# import os

def take_log():

    logging.basicConfig(filename='record.log', level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
