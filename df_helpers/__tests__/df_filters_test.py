import df_helpers.ct_df_filters as ct
import pandas as pd

d = {'test_col_1': ['foo','bar','baz','foo','bar','foo','foofoo', None], 'test_col_2': ['test1','test2','test3','test4','test5','test6','test7',None]}

def test_filter_single_string_exact():
    df = pd.DataFrame(d)
    filtered = ct.filter_string_column(df,'test_col_1','foo',True)
    assert filtered.shape[0] == 3

def test_filter_single_string_contains():
    df = pd.DataFrame(d)
    filtered = ct.filter_string_column(df,'test_col_1','foo')
    assert filtered.shape[0] == 4