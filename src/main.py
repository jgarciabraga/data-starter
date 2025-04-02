import data_starter.extract as extract
import data_starter.load as load
import data_starter.transform as transform
import data_starter.generate_data as generate_data

if __name__ == '__main__':
    path_dir_input = "data/input"
    generate_data.generate_data(50, path_dir_input)
    data_frame_list = extract.extract_from_excel(path_dir_input)
    data_frame = transform.concat_dataframe_list(data_frame_list)
    print(load.load_data(data_frame, 'output.xlsx', 'data/output'))
