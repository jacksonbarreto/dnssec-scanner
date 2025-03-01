from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from src.analyzer.utils.color_format_chart_bar import format_bar_annotations
from src.analyzer.utils.wrap_labels import wrap_labels

CHART_WIDTH: int = 8
MIN_HEIGHT: int = 6


def make_bar_chart(stats_df: pd.DataFrame, y_column: str, x_label: str, y_label: str, title: str, legend_title: str,
                   color_map: list[str],
                   legend_position: str = None, legend_columns: int = None, bbox_to_anchor: Tuple[int, int] = None,
                   ) -> Figure:
    legend_position = "lower left" if legend_position is None else legend_position
    legend_columns = 6 if legend_columns is None else legend_columns
    bbox_to_anchor = (0, 1) if bbox_to_anchor is None else bbox_to_anchor

    columns_to_plot = [col for col in stats_df.columns.tolist() if col not in [y_column]]
    stats_df.set_index(y_column, inplace=True)
    size_box = (CHART_WIDTH, max(MIN_HEIGHT, int(len(stats_df) * 0.35)))
    fig, ax = plt.subplots(figsize=size_box)

    stats_df.plot(kind='barh', stacked=True, edgecolor="black", ax=ax, color=color_map)
    format_bar_annotations(ax)

    #ax.set_title(title, fontsize=16, pad=55, y=1)
    fig.suptitle(title, fontsize=16, y=0.98, horizontalalignment='center')
    ax.set_xlabel(x_label, fontsize=12)
    ax.set_ylabel(y_label, fontsize=12)
    # ax.set_yticklabels(wrap_labels(stats_df.index))

    ax.legend(columns_to_plot, title=legend_title, loc=legend_position, bbox_to_anchor=bbox_to_anchor,
              ncol=legend_columns,
              frameon=False)
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    plt.tight_layout()
    return fig
