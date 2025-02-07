import logging
import os
import re

from src.config.paths import DATA_SOURCE_DIRECTORY
from src.scanner.dnssec import scan
from src.utils.logging_setup import logging_setup


def main():
    logging_setup()

    files: list[str] = [f for f in os.listdir(DATA_SOURCE_DIRECTORY) if re.match(r'^[a-zA-Z]{2}-.*\.csv$', f)]

    if not files:
        logging.warning(
            f"No CSV files found in '{DATA_SOURCE_DIRECTORY}'. Please ensure the files are in the correct directory."
            f"\n The expected format is 'country_platform.csv', where country is the ISO 3166-1 alpha-2 code and platform is the platform name."
        )
        return

    logging.info(f"Found {len(files)} files to scan.")

    for file in files:
        file_path: str = os.path.join(DATA_SOURCE_DIRECTORY, file)
        try:
            logging.info(f"Scanning file: {file}")
            scan(file_path)
            logging.info(f"Scan complete for {file}")
        except Exception as e:
            logging.error(f"Error scanning {file}: {e}")


if __name__ == "__main__":
    main()
