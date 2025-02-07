import os

ROOT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')

LOG_FILE = os.path.join(ROOT_DIRECTORY, 'scan.log')
DATA_SOURCE_DIRECTORY = os.path.join(ROOT_DIRECTORY, 'src', 'data', 'source')