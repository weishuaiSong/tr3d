import pickle
import os
import argparse
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


def merge_scannet_data():
    file_path = './data/scannet'
    file_path1 = './data/scannet/scannet_infos_val.pkl'
    file_path2 = './data/scannet/scannet_infos_train.pkl'

    # Load data from val file
    with open(file_path1, 'rb') as file:
        data1 = pickle.load(file)

    # Load data from train file
    with open(file_path2, 'rb') as file:
        data2 = pickle.load(file)

    # Merge data
    merged_data = data1 + data2

    # Save merged data
    merged_file_path = os.path.join(file_path, 'scannet_infos.pkl')
    with open(merged_file_path, 'wb') as file:
        pickle.dump(merged_data, file)

    print(f"Merged data saved to {merged_file_path}")

def merge_scannet_data():
    file_path = './data/scannet'
    file_path1 = './data/scannet/scannet_infos_val.pkl'
    file_path2 = './data/scannet/scannet_infos_train.pkl'

    # Load data from val file
    with open(file_path1, 'rb') as file:
        data1 = pickle.load(file)

    # Load data from train file
    with open(file_path2, 'rb') as file:
        data2 = pickle.load(file)

    # Merge data
    merged_data = data1 + data2

    # Save merged data
    merged_file_path = os.path.join(file_path, 'scannet_infos.pkl')
    with open(merged_file_path, 'wb') as file:
        pickle.dump(merged_data, file)

    print(f"Merged data saved to {merged_file_path}")

def merge_s3dis_data():
    combined_data = []
    input_directory = "./data/s3dis"
    output_file = "./data/s3dis/s3dis_infos.pkl"
    
    for i in range(1, 7):
        filename = f"s3dis_infos_Area_{i}.pkl"
        file_path = os.path.join(input_directory, filename)
        
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                data = pickle.load(f)
                if isinstance(data, list):
                    combined_data.extend(data)
                else:
                    print(f"Warning: Data in {filename} is not in list format")
        else:
            print(f"Warning: File {filename} does not exist")
    
    with open(output_file, 'wb') as f:
        pickle.dump(combined_data, f)

def main():
    parser = argparse.ArgumentParser(description="Merge dataset information files.")
    parser.add_argument("--datasets", nargs='+', choices=['sunrgbd', 'scannet', 's3dis'], 
                        help="Specify which datasets to merge (e.g., --datasets sunrgbd scannet)")
    
    args = parser.parse_args()
    
    if not args.datasets:
        print("No datasets specified. Please use --datasets to specify which datasets to merge.")
        return

    for dataset in args.datasets:
        if dataset == 'sunrgbd':
            merge_sunrgbd_data()
        elif dataset == 'scannet':
            merge_scannet_data()
        elif dataset == 's3dis':
            merge_s3dis_data()

if __name__ == "__main__":
    merge_sunrgbd_data()
    merge_scannet_data()
    merge_s3dis_data()
