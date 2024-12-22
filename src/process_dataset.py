import argparse
import json

def process_dataset(input_file, output_file, min_duplicate=2):
    """
    处理数据集文件，过滤掉重复数小于 min_duplicate 的样本。

    参数：
    - input_file: 输入的 dataset.index 文件路径
    - output_file: 输出的过滤后文件路径
    - min_duplicate: 最小重复次数，低于该值的样本将被过滤
    """
    # 读取原始 dataset.index 文件
    with open(input_file, 'r') as infile:
        data = json.load(infile)

    # 过滤 samples，保留 duplicate >= min_duplicate 的样本
    filtered_samples = [
        sample for scene in data['scenes'] for sample in scene['samples'] if sample['duplicate'] >= min_duplicate
    ]
    
    # 更新数据
    data['samples'] = filtered_samples

    # 将过滤后的数据保存到输出文件
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4)
    
    print(f"Processed dataset saved to {output_file}")

def main():
    # 使用 argparse 处理命令行参数
    parser = argparse.ArgumentParser(description="Filter dataset.index based on duplicate count.")
    parser.add_argument("input_file", help="Input dataset.index file path")
    parser.add_argument("output_file", help="Output filtered dataset file path")
    parser.add_argument("--min_duplicate", type=int, default=2, help="Minimum duplicate count for keeping samples (default: 2)")
    
    args = parser.parse_args()

    # 调用处理函数
    process_dataset(args.input_file, args.output_file, args.min_duplicate)

if __name__ == "__main__":
    main()
