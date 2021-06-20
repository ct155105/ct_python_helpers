import pandas as pd

def filter_string_column(df: pd.DataFrame, column: str, value: str or list, exact: bool = False) -> pd.DataFrame:
    """Gets and prints the spreadsheet's header columns

    Args:
        df: The DataFrame to filter
        column: The column to filter on
        value: The string or list of strings containing the values to filter on
        exact: The value must match exactly. Can be substring if false.

    Returns:
        the origin dataframe filtered
    """

    if exact:
        result = df[df[column].eq(value)]
        return result

    result = df[df[column].str.contains(value,na=False)]
    return result