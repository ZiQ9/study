import argparse
import os
import cv2

parser = argparse.ArgumentParser(description='img_dir内の画像をすべてグレースケールにする')

parser.add_argument('arg1', help='受け取る画像が入ったディレクトリ')
parser.add_argument('arg2', help='出力するディレクトリ')
parser.add_argument('--arg3')

args = parser.parse_args()

input_dir_path = args.arg1
file_list = os.listdir(args.arg1)

if not os.path.exists(args.arg2):
    os.makedirs(args.arg2)

for file_name in file_list:
    root, ext = os.path.splitext(file_name)
    if ext == '.png' or '.jpeg' or '.jpg':
        abs_name = input_dir_path + '/' + file_name
        image = cv2.imread(abs_name)

        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("args.arg2/output.jpg", image_gray)
