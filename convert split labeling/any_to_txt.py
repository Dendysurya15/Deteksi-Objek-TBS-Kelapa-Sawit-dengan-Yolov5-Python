
from email import parser
import os
import argparse
from pathlib import Path
# return all files as a list
# dirname = r'D:\FILE\gradingAI\sampel_cctv_baru\label\eli\10.9.143.25_01_20220414121122557'
parser = argparse.ArgumentParser() 
parser.add_argument('--dir', type=str)
dirname = parser.parse_args().dir

for file in os.listdir(dirname):
     # check the files which are end with specific extension
    if file.endswith(".jpg"):
        # print path name of selected files
        # print(file)
        namefile = file.rsplit('.', 1)[0]
        txt = Path(dirname+'/'+namefile+'.txt')
        xml = Path(dirname+'/'+namefile+'.xml')
        if txt.is_file() or xml.is_file():
            print(namefile + ' sudah ada label')
        else:
            file1 = open(dirname+'/'+namefile+'.txt', "w")
            file1.write("")
            print(namefile + ' label kosong telah dibuat')
            file1.close()
        # with open.(os)
