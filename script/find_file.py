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
countNotXML = 0
countFile = 0

print('test')
if os.path.isdir(output_folder) != True:
    os.makedirs(output_folder)

arrIn = []

with open(input_txt, 'r') as z:
    for line in z:
        arrIn.append(line.strip())

arrFile = arrIn

a=0



for path, subdirs, files in os.walk(input_folder):
    for name in files:
        for x in arrIn:
            if fnmatch(name, x + ".jpg") or fnmatch(name, x + ".jpeg"):
                arrFile.remove(x)
                a+=1
                #copy this file to output folder
                try:
                    shutil.move(path  + name, output_folder + name)
                    shutil.move(path  + x + ".txt", output_folder + x + ".txt")
                except:
                    print('file tidak ada bos')
                if xml:
                    try:
                        countFile=countFile+1
                        shutil.move(path  + x + ".xml", output_folder)
                        print("File " + str(name) + " sudah dicopy" + " | Count=" + str(countFile) + " | NoXML=" +  str(countNotXML) + " | Sisa=" + str(len(arrFile)))
                    except:
                        countNotXML=countNotXML+1
                        print("Tidak ada file xml " + str(name) + " | Count=" + str(countFile) + " | NoXML=" +  str(countNotXML) + " | Sisa=" + str(len(arrFile)))

with open(path + "/sisa.txt", "a") as f:
    for o in arrFile:
        f.write(o + "\n")


                
                    

