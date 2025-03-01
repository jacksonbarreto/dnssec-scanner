import os
from typing import Tuple
import matplotlib.pyplot as plt
import pandas as pd

from src.analyzer.utils.dataframe_stats import get_dataframe_stats
from src.analyzer.utils.get_country_name import get_country_name
from src.analyzer.utils.make_bar_chart import make_bar_chart
from src.analyzer.utils.save_chart import save_chart
from src.config.paths import CHART_DIRECTORY


def generate_bar_charts(consolidated_dataframe: pd.DataFrame, target_column, title_prefix,
                        color_map: list[str],
                        x_label: str = None, y_label: str = None, title: str = None, legend_title: str = None,
                        legend_position: str = None, legend_columns: int = None, bbox_to_anchor: Tuple[int, int] = None,
                        columns_to_sort: list[str] = None, ascending=False):

    columns_to_sort = [] if columns_to_sort is None else columns_to_sort
    legend_title = title_prefix if legend_title is None else legend_title
    countries = consolidated_dataframe["country"].unique()
    rename_map = {
        "NUTS2_Label_2016": "NUTS2",
    }
    filenames: list[str] = []
    for country in countries:
        group_by = ["country", "NUTS2_Label_2016"]
        stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map)

        data = stats_df[stats_df["country"] == country].drop(columns=["country"]).sort_values(by=columns_to_sort,
                                                                                              ascending=ascending)
        label: str = f"{title_prefix.replace(' ', '_').lower()}_in_{get_country_name(country).lower()}_by_nuts2"
        chart = make_bar_chart(data, "NUTS2", f"{title_prefix} (%)", "NUTS2",
                               f"{title_prefix} in {get_country_name(country)} by NUTS2 (%)", legend_title,color_map)
        filename: str = f"{label}.pdf"
        chart.savefig(os.path.join(CHART_DIRECTORY, filename), format="pdf", bbox_inches="tight")
        filenames.append(filename)
        plt.show()
        plt.close(chart)
        group_by = ["country", "NUTS2_Label_2016", "Category"]
        stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map)
        for _, category in enumerate(["public", "private"]):
            data = stats_df[(stats_df["country"] == country) & (stats_df["Category"] == category)].drop(
                columns=["country", "Category"]).sort_values(by=columns_to_sort, ascending=ascending)
            label = f"{title_prefix.replace(' ', '_').lower()}_at_{category}_hei_in_{get_country_name(country).lower()}_by_nuts2"
            if not data.empty:
                chart = make_bar_chart(data, "NUTS2", f"{title_prefix} (%)", "NUTS2",
                                       f"{title_prefix} at {category.capitalize()} HEIs in {get_country_name(country)} (%)", legend_title, color_map)
                filename = f"{label}.pdf"
                chart.savefig(os.path.join(CHART_DIRECTORY, filename), format="pdf", bbox_inches="tight")
                filenames.append(filename)
                plt.show()
                plt.close(chart)

    group_by = ["country"]
    rename_map = {"country": "Country"}
    stats_df = get_dataframe_stats(consolidated_dataframe, target_column, group_by, rename_map).sort_values(
        by=columns_to_sort, ascending=ascending)
    stats_df["Country"] = stats_df["Country"].map(lambda x: get_country_name(x))
    label = f"{title_prefix.replace(' ', '_').lower()}_by_country"
    chart = make_bar_chart(stats_df, "Country", f"{title_prefix} (%)", "Country",
                           f"{title_prefix} by Country (%)",
                           legend_title, color_map)
    filename = f"{label}.pdf"
    chart.savefig(os.path.join(CHART_DIRECTORY, filename), format="pdf", bbox_inches="tight")
    filenames.append(filename)
    plt.show()
    plt.close(chart)
    input_text: str = "".join(f"""
\\begin{{figure}}[H]
    \\centering
    \\includegraphics[width=1\\textwidth]{{figs/dnssec/{f}}}
    \\caption{{{f.split('.')[0].replace('_',' ').title()}}}
    \\label{{fig:{f.split('.')[0]}}}
\\end{{figure}} \n\n""" for f in filenames)
    save_chart(input_text, f"{title_prefix.replace(' ', '_').lower()}_INPUTS.txt")