import pandas as pd
import numpy as np


def trim_col_names(df: pd.DataFrame) -> pd.DataFrame:
    '''Removes spaces from column names
    
        Args:
            df: The DataFrame whose columns will be trimmed

        Returns:
            The original dataframe with trimmed column names

    '''

    new_cols = {}
    for col in df.columns:
        new_cols[col] = col.replace(" ",'')
    renamed_df = df.rename(new_cols, axis=1)

    return renamed_df
        

def date_column_str_to_epoch(df: pd.DataFrame, column: str) -> pd.DataFrame:
    '''Converts a column that is currently a date as string to epoch int
    
    Args:
        df: The DataFrame housing the column to convert
        column: The name of the column to convert

    Returns:
        The dataframe with the column converted to epoch
    '''

    df2 = df.copy()
    df2[column] = pd.to_datetime(df2[column]).values.astype(np.int64)

    return df2