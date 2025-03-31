import data_starter.extract as extract
import data_starter.load as load
import data_starter.transform as transform

if __name__ == '__main__':
    data_frame_list = extract.extract_from_excel('data/input')
    data_frame = transform.concat_dataframe_list(data_frame_list)
    print(load.load_data(data_frame, 'output.xlsx', 'data/output'))
