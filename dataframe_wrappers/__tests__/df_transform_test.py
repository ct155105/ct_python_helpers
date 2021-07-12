import df_helpers.df_transformers as ct
import pandas as pd

def test_trim_column_names():
    data = {'col 1': [1,2,3], 'col2': [1, 2, 3], 'COL   3': [1,2,3]}
    df = pd.DataFrame(data)
    df = ct.trim_col_names(df)

    test = df.columns == ['col1','col2','COL3']

    assert test.all()


def test_date_column_str_to_epoch():
    d = {"date_col": ['1995/08/25 05:00:00+00']}
    df = pd.DataFrame(d)
    df = ct.date_column_str_to_epoch(df,'date_col')

    assert df.iloc[0]['date_col'] == 809326800000000000