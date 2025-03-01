import pandas as pd

from src.analyzer.utils.dataframe_stats import get_dataframe_stats
from src.analyzer.utils.get_country_name import get_country_name
from src.analyzer.utils.get_latex_table import get_latex_table
from src.analyzer.utils.remove_empty_columns import remove_empty_columns
from src.analyzer.utils.save_table import save_table


def generate_tables(consolidated_dataframe: pd.DataFrame, target_column, title_prefix,
                    columns_to_sort: list[str] = None, ascending=False, avg=False):
    if columns_to_sort is None:
        columns_to_sort = []
    countries = consolidated_dataframe["country"].unique()
    rename_map = {
        "NUTS2_Label_2016": "NUTS2",
    }
    if "score" in consolidated_dataframe.columns:
        rename_map.update({"score": "Score"})
    filenames: list[str] = []
    for country in countries:
        group_by = ["country", "NUTS2_Label_2016"]
        stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map, avg)

        data = stats_df[stats_df["country"] == country].drop(columns=["country"]).sort_values(by=columns_to_sort,
                                                                                              ascending=ascending)
        remove_empty_columns(data)
        label: str = f"{title_prefix.replace(' ', '_').lower()}_in_{country.lower()}_by_nuts2"
        table = get_latex_table(data, f"{title_prefix} in {get_country_name(country)} by NUTS2 (\\%)", label)
        filename: str = f"{label}.tex"
        save_table(table, filename)
        filenames.append(filename)

        group_by = ["country", "NUTS2_Label_2016", "Category"]
        stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map, avg)
        for _, category in enumerate(["public", "private"]):
            data = stats_df[(stats_df["country"] == country) & (stats_df["Category"] == category)].drop(
                columns=["country", "Category"]).sort_values(by=columns_to_sort, ascending=ascending)
            remove_empty_columns(data)
            label = f"{title_prefix.replace(' ', '_').lower()}_in_{country.lower()}_by_nuts2_{category}"
            table = get_latex_table(
                data,
                f"{title_prefix} at {category.capitalize()} HEIs in {get_country_name(country)} by NUTS2 (\\%)", label)
            filename = f"{label}.tex"
            save_table(table, filename)
            filenames.append(filename)

    group_by = ["country"]
    rename_map = {"country": "Country"}
    if "score" in consolidated_dataframe.columns:
        rename_map.update({"score": "Score"})
    stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map, avg).sort_values(
        by=columns_to_sort, ascending=ascending)
    stats_df["Country"] = stats_df["Country"].map(lambda x: get_country_name(x))
    remove_empty_columns(stats_df)
    label = f"{title_prefix.replace(' ', '_').lower()}_by_country"
    table = get_latex_table(stats_df, f"{title_prefix} by Country (\\%)",label)
    filename = f"{label}.tex"
    save_table(table, filename)
    filenames.append(filename)
    # \input{tables/dnssec/key_algorithm_distribution_by_country}
    input_text: str = "".join(f"\\input{{tables/dnssec/{f.split(".")[0]}}} \n\n" for f in filenames)
    save_table(input_text, f"{title_prefix.replace(' ', '_').lower()}_INPUTS.txt")
