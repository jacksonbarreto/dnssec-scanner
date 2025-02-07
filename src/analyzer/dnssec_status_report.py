import pandas as pd

from src.config.paths import CONSOLIDATED_RESULT_TO_ANALYZE


def generate_dnssec_status_report(consolidated_dataframe: pd.DataFrame = None):
    if consolidated_dataframe is None:
        consolidated_dataframe = pd.read_csv(CONSOLIDATED_RESULT_TO_ANALYZE)

if __name__ == "__main__":
    generate_dnssec_status_report()
