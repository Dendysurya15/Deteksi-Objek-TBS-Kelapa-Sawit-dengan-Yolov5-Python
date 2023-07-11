from ast import If
import os
import argparse
from fnmatch import fnmatch
import shutil
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument('--input_folder', type=str, default=str(os.getcwd()) + '/rekap', help='input folder path')
parser.add_argument('--output_folder', type=str, default=str(os.getcwd()) + '/output', help='output folder path')
parser.add_argument('--input_txt', type=str, help='input txt')
parser.add_argument('--xml', default=True, type=bool, help='is XML?')

input_folder = parser.parse_args().input_folder
output_folder = parser.parse_args().output_folder
input_txt = parser.parse_args().input_txt
xml = parser.parse_args().xml

if os.path.isdir(output_folder) != True:
    os.makedirs(output_folder)

arrIn = []
copied = []

#print("Dalam list:")
with open(input_txt, 'r') as z:
    for line in z:
        arrIn.append(line.strip())
        print(str(line.strip()))
        
for path, subdirs, files in os.walk(input_folder):
    for name in files:
        if fnmatch(name, "*.JPG") or fnmatch(name, "*.jpg") or fnmatch(name, "*.JPEG") or fnmatch(name, "*.jpeg") and not fnmatch(name, "*.txt"):
            status = True
            for x in arrIn:
               # print ("match: x:" + x + " name:" + name)
                if fnmatch(name, x + ".JPG") or fnmatch(name, x+ ".jpg") or fnmatch(name, x+".JPEG") or fnmatch(name, x+".jpeg"):
                    status = False
                    print("File " + str(name) + " TDK DICOPY")
                    break
            #copy this file to output folder
            if status:
                print("File " + str(name) + " sudah dicopy")
                if len(name.split(".")[-1]) == 3:
                    file_name = (os.path.join(path, name[0:-4]))
                elif len(name.split(".")[-1]) == 4:    
                    file_name = (os.path.join(path, name[0:-5]))
                shutil.copy(path + "/" + name, output_folder)
                shutil.copy(file_name + ".txt", output_folder)
                if xml:
                    try:
                        shutil.copy(file_name + ".xml", output_folder)
                    except:
                        print("Tidak ada file xml")
                    
                
                    

