import argparse
parser = argparse.ArgumentParser()
parser.add_argument('indir', type=str, help='директория из которой будет взят файл')
parser.add_argument('-file_name', type=str, help='имя файла')
args = parser.parse_args()
print(args.indir)
print(args.file_name)