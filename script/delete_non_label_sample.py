 # Import Module
from ast import If
from logging import Logger
import os
import argparse
from fnmatch import fnmatch
import shutil

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Read text File
def read_text_file(file_path, output):
    filesize = os.path.getsize(file_path)
    jpeg_min = file_path[0:-4]+".jpg"
    jpeg_max = file_path[0:-4]+".JPG"
    if filesize != 0:
        try:        
            try:
                shutil.copy(jpeg_min, output)
            except:
                try:
                    shutil.copy(jpeg_max, output)
                except:
                    print(bcolors.FAIL + "Error:" + jpeg_max + " JPEG file is not found!" + bcolors.ENDC)
            shutil.copy(file_path, output)
        except:
            print(bcolors.FAIL + "Error:" + file_path + " TXT file is not found!" + bcolors.ENDC)
    
    elif filesize == 0:
        kosong_path = output + "/kosong"
        if os.path.isdir(kosong_path) != True:
            os.makedirs(kosong_path)
                
        try:
            shutil.copy(jpeg_min, kosong_path)
        except:
            try:
                shutil.copy(jpeg_max, output)
            except:
                print(bcolors.FAIL + "Error:" + jpeg_max + " JPEG file is not found!" + bcolors.ENDC)
                
        shutil.copy(file_path, kosong_path)


parser = argparse.ArgumentParser()

parser.add_argument('--output_folder', nargs='+', type=str, help='folder path')
parser.add_argument('--input', nargs='+', type=str, help='folder path')

output = str(parser.parse_args().output_folder)[2:-2]
folder = str(parser.parse_args().input)[2:-2]

if os.path.isdir(output) != True:
    os.makedirs(output)

# Change the directory
os.chdir(folder)


for path, subdirs, files in os.walk(folder):
    for name in files:
        if fnmatch(name, "*.TXT") or fnmatch(name, "*.txt"):
            #print(os.path.join(path, name))
            read_text_file(os.path.join(path, name), output)

""" 
# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"

		# call read text file function
		read_text_file(file_path)
 """
