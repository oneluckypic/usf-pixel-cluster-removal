
import pandas as pd
import yaml

from usf_pcr.labels import via_dict_to_dataframe


def test_via_dict_to_dataframe(via_proj, via_dataframe):
        df = via_dict_to_dataframe(via_proj)
        pd.testing.assert_frame_equal(df, via_dataframe)
