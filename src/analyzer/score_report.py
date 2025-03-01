import pandas as pd

from src.analyzer.utils.generate_tables import generate_tables
from src.config.paths import CONSOLIDATED_RESULT_TO_ANALYZE


def generate_score_report(consolidated_dataframe: pd.DataFrame | None = None):
    if consolidated_dataframe is None:
        consolidated_dataframe = pd.read_csv(CONSOLIDATED_RESULT_TO_ANALYZE)
    generate_tables(consolidated_dataframe, "score", "DNSSEC Average Score", columns_to_sort=["Score"], avg=True)

if __name__ == "__main__":
    generate_score_report()
