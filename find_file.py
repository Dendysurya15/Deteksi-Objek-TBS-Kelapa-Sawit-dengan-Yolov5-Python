from ast import If
import os
import argparse
from fnmatch import fnmatch
import shutil
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', type=str, default=str(os.getcwd()) + '/rekap', help='input folder path')
parser.add_argument('--output_folder', type=str, default=str(os.getcwd()) + '/output', help='output folder path')
parser.add_argument('--array', type=str, help='input array')

input_folder = parser.parse_args().input_folder
output_folder = parser.parse_args().output_folder
arrIn = parser.parse_args().array.split(',')

print('test')
if os.path.isdir(output_folder) != True:
    os.makedirs(output_folder)

a=0
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        for x in arrIn:
            if fnmatch(name, x + ".jpg"):
                a+=1
                print("File " + str(a) + " sudah dicopy")
                #copy this file to output folder
                shutil.copy(path + "/" + name, output_folder)
                shutil.copy(path + "/" + name.replace("jpg", "txt", 1), output_folder)
                # shutil.copy(path+name-jpg+txt, output_folder)

