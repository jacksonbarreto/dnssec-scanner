import pandas as pd

from src.config.paths import CONSOLIDATED_RESULT_TO_ANALYZE


def get_dataframe_stats(dataframe: pd.DataFrame, target_column: str, group_by: list[str],
                        rename_map: dict[str, str] = None, avg: bool = False) -> pd.DataFrame:
    if avg:
        df_stats = dataframe.groupby(group_by).agg({target_column: lambda x: round(x.mean(), 2)}).reset_index()
        return df_stats.rename(columns={} if rename_map is None else rename_map)
    else:
        df_stats = dataframe.groupby(group_by + [target_column]).size().unstack(fill_value=0).reset_index()

    df_stats.columns.name = None
    key_contents = dataframe[target_column].unique()
    df_stats["total"] = df_stats[key_contents].sum(axis=1)
    for key in key_contents:
        df_stats[f"{key}_percent"] = (
                df_stats[key] / df_stats["total"] * 100).round(2)
    df_stats.drop(columns=key_contents.tolist() + ["total"], inplace=True)
    rename_map = {} if rename_map is None else rename_map
    rename_map.update(**{col: col.replace("_percent", "") for col in df_stats.columns if col.endswith("_percent")})
    df_stats.rename(columns=rename_map, inplace=True)
    return df_stats


if __name__ == "__main__":
    df = pd.read_csv(CONSOLIDATED_RESULT_TO_ANALYZE)
    df["total"] = 0
    # stats = df.groupby(["country", "NUTS2_Label_2016", "Category"]).agg({"score": lambda x: round(x.mean(), 2)}).reset_index()
    a = get_dataframe_stats(df, "score", ["country", "NUTS2_Label_2016"], avg=True)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)

    print(a.head())
