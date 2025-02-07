_config: dict[str, str | int] = {
    "max_workers": 5,
    "url_base_api": "https://dns.google/resolve",
    "error_column": "error",
    "errors_folder": "errors",
    "results_folder": "results",
}


class Config:
    @staticmethod
    def get_max_workers() -> int:
        return _config.get("max_workers", 5)

    @staticmethod
    def get_url_base_api() -> str:
        return _config.get("url_base_api", "https://dns.google/resolve")

    @staticmethod
    def get_error_column() -> str:
        return _config.get("error_column", "error")

    @staticmethod
    def get_errors_folder() -> str:
        return _config.get("errors_folder", "errors")

    @staticmethod
    def get_results_folder() -> str:
        return _config.get("results_folder", "results")
