import os

import pandas as pd


def load_data(df: pd.DataFrame, file_name: str, output_folder: str) -> bool:
    """
    function receives a dataframe, file name and folder and save it as a excel file \n
    return true if the dataframe was saved and false if not \n
    type: df: pandas.DataFrame \n
    type: file_name: str \n
    type: output_folder: str \n
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    try:
        final_file = os.path.join(output_folder, file_name)
        df.to_excel(final_file, index=False)
        return True
    except:
        return False
