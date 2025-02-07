import logging
import os
import re
import pandas as pd

from src.config.config import Config
from src.config.paths import DATA_RESULTS_DIRECTORY, CONSOLIDATED_RESULT_TO_ANALYZE


def generate_consolidated_data() -> pd.DataFrame:
    files: list[str] = [f for f in os.listdir(DATA_RESULTS_DIRECTORY) if re.match(r'^[a-zA-Z]{2}_.*\.csv$', f)]

    if not files:
        logging.warning(
            f"No CSV files found in '{DATA_RESULTS_DIRECTORY}'. Please ensure the files are in the correct directory."
            f"\n The expected format is 'country_platform.csv', where country is the ISO 3166-1 alpha-2 code and platform is the platform name."
        )
        return

    logging.info(f"Found {len(files)} files to scan.")

    dataframes: list[pd.DataFrame] = []
    for file in files:
        file_path: str = os.path.join(DATA_RESULTS_DIRECTORY, file)
        try:
            country_code: str = os.path.basename(file_path)[:2]
            logging.info(f"Loading file: {file} (Country: {country_code})")

            df: pd.DataFrame = pd.read_csv(file_path)
            df[Config.get_country_column()] = country_code
            df = df.loc[df.groupby(Config.get_id_column())[Config.get_score_column()].idxmin()]
            dataframes.append(df)

        except Exception as e:
            logging.error(e)

    try:
        consolidated_dataframe: pd.DataFrame = pd.concat(dataframes, ignore_index=True)
        consolidated_dataframe.to_csv(CONSOLIDATED_RESULT_TO_ANALYZE, index=False, encoding='utf-8')
        logging.info(f"Consolidated data saved in: {CONSOLIDATED_RESULT_TO_ANALYZE}")
        return consolidated_dataframe
    except Exception as e:
        logging.error(e)
        raise e