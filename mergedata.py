import pickle
import os

def merge_sunrgbd_data():
    file_path = './data/sunrgbd'
    file_path1 = './data/sunrgbd/sunrgbd_infos_val.pkl'
    file_path2 = './data/sunrgbd/sunrgbd_infos_train.pkl'

    # Load data from val file
    with open(file_path1, 'rb') as file:
        data1 = pickle.load(file)

    # Load data from train file
    with open(file_path2, 'rb') as file:
        data2 = pickle.load(file)

    # Merge data
    merged_data = data1 + data2

    # Save merged data
    merged_file_path = os.path.join(file_path, 'sunrgbd_infos.pkl')
    with open(merged_file_path, 'wb') as file:
        pickle.dump(merged_data, file)

    print(f"Merged data saved to {merged_file_path}")

if __name__ == "__main__":
    merge_sunrgbd_data()