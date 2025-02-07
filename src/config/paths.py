import os

from src.config.config import Config

ROOT_DIRECTORY: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
DATA_BASE_DIRECTORY: str = os.path.join(ROOT_DIRECTORY, 'src', 'data')
DATA_SOURCE_DIRECTORY: str = os.path.join(DATA_BASE_DIRECTORY, 'source')
DATA_RESULTS_DIRECTORY: str = os.path.join(DATA_BASE_DIRECTORY, Config.get_results_folder())
DATA_ERRORS_DIRECTORY: str = os.path.join(DATA_BASE_DIRECTORY, Config.get_errors_folder())
REPORT_DIRECTORY:str = os.path.join(DATA_BASE_DIRECTORY, 'reports')
TABLE_DIRECTORY: str = os.path.join(REPORT_DIRECTORY, 'tables')
CHART_DIRECTORY: str = os.path.join(REPORT_DIRECTORY, 'charts')
LOG_FILE: str = os.path.join(ROOT_DIRECTORY, 'scan.log')
