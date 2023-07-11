from ast import If
import os
import argparse
from fnmatch import fnmatch
import shutil
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', type=str, default=str(os.getcwd()) + '/rekap', help='input folder path')
parser.add_argument('--output_folder', type=str, default=str(os.getcwd()) + '/output', help='output folder path')

input_folder = parser.parse_args().input_folder
output_folder = parser.parse_args().output_folder

if os.path.isdir(output_folder) != True:
    os.makedirs(output_folder)

arrJPEG = []
arrXML = []
  
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        if fnmatch(name, "*.JPG") or fnmatch(name, "*.jpg") or fnmatch(name, "*.JPEG") or fnmatch(name, "*.jpeg"):
            arrName = name.split(".")
            arrJPEG.append(arrName[0])

for path, subdirs, files in os.walk(input_folder):
    for name in files:
        if fnmatch(name, "*.XML") or fnmatch(name, "*.xml"):
            for x in arrJPEG:
                arrName = name.split(".")
                if fnmatch(x,arrName[0]):
                    arrXML.append(arrName[0])

diff = set(arrJPEG) - set(arrXML)

with open(output_folder + "/0lebihXML.txt", "a") as f:
    for o in diff:
        f.write(o + "\n")





                    
                
                    

