import json
import argparse
import os

def merge_datasets(input_files, output_file):
    """
    合并多个数据集文件到一个文件。
    
    :param input_files: 要合并的数据集文件路径列表
    :param output_file: 合并后保存的文件路径
    """
    merged_data = []
    
    # 读取每个输入文件并合并数据
    for file in input_files:
        with open(file, 'r') as f:
            data = json.load(f)
            merged_data.extend(data)
    
    # 写入到输出文件
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w') as f:
        json.dump(merged_data, f)
    
    print(f"Merged {len(input_files)} datasets into {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge datasets")
    parser.add_argument("input_files", nargs='+', help="List of dataset files to merge")
    parser.add_argument("output_file", help="Path to the output merged dataset file")
    
    args = parser.parse_args()
    
    merge_datasets(args.input_files, args.output_file)
