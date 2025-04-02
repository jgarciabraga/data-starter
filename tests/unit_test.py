import os
import pandas as pd
import pytest
import src.data_starter.extract as extract
import src.data_starter.transform as transform
import src.data_starter.load as load

@pytest.fixture
def mock_inputfolder(tmp_path):

    df_1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df_2 = pd.DataFrame({"a": [5, 6], "b": [7, 8]})

    file_1 = os.path.join(tmp_path, "file_1.xlsx")
    file_2 = os.path.join(tmp_path, "file_2.xlsx")
    df_1.to_excel(file_1, index=False)
    df_2.to_excel(file_2, index=False)

    return tmp_path, [df_1, df_2]

@pytest.fixture
def mock_cocatenate_data():

    df_1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df_2 = pd.DataFrame({"a": [5, 6], "b": [7, 8]})
    list_dataframes = [df_1, df_2]
    df_final = pd.concat(list_dataframes, ignore_index=True)

    return list_dataframes, df_final

@pytest.fixture
def mock_outputfolder(tmp_path):
    output_folder = tmp_path / "output_folder"
    output_folder.mkdir()
    return str(output_folder)

def test_extract(mock_inputfolder):
    test_path, test_dataframe_list = mock_inputfolder
    dataframe_list = extract.extract_from_excel(test_path)

    assert len(test_dataframe_list) == len(dataframe_list)
    
    test_names = []
    names = []
    
    for df_test in test_dataframe_list:
        for test_column_name in df_test.columns.tolist():
            test_names.append(test_column_name)
    
    for df in dataframe_list:
        for column_name in df.columns.tolist():
            names.append(column_name)
        

    assert list(set(test_names)) == list(set(names))

    for df_res, df_test in zip(dataframe_list, test_dataframe_list):
        pd.testing.assert_frame_equal(df_res, df_test)

def test_transform(mock_cocatenate_data):
    test_list_dataframes, test_df_final = mock_cocatenate_data
    res_df_final = transform.concat_dataframe_list(test_list_dataframes)

    assert len(res_df_final) == len(test_df_final)

    pd.testing.assert_frame_equal(res_df_final, test_df_final)

def test_load(mock_outputfolder):

    df_1 = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    df_2 = pd.DataFrame({"a": [5, 6], "b": [7, 8]})
    test_df_final = pd.concat([df_1, df_2], ignore_index=True)

    file_name = "test_output.xlsx"

    load.load_data(test_df_final, file_name, mock_outputfolder) == True
    assert os.path.exists(os.path.join(mock_outputfolder, file_name))
    
    ld_df = pd.read_excel(os.path.join(mock_outputfolder, file_name))
    pd.testing.assert_frame_equal(ld_df, test_df_final)




