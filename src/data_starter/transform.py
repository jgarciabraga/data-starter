from typing import List

import pandas as pd


def concat_dataframe_list(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)
