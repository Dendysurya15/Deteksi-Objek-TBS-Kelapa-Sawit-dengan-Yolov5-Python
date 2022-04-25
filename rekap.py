 # Import Module
from ast import If
import os
import argparse
from fnmatch import fnmatch

# Read text File
def read_text_file(file_path, output):
	with open(file_path, 'r') as z:
		content = z.readlines()
		file_path = output + '/rekap/rekap.TXT'
		dir_path = output + '/rekap'
		if os.path.isdir(dir_path) != True:
				os.makedirs(output + '/rekap')
		try:
			write_text_file(file_path, content[1])
		except:
			write_text_file(file_path, content[0])
		z.close()

def write_text_file(output, text):
    with open(output, 'a') as f:
        f.write('\n' + text)
        f.close()

parser = argparse.ArgumentParser()
parser.add_argument('--folder', nargs='+', type=str, default=str(os.getcwd()) + '/rekap', help='folder path')
folder = parser.parse_args().folder
parser.add_argument('--output', nargs='+', type=str, default=str(os.getcwd()) + '/output', help='folder path')
output = parser.parse_args().output

# Change the directory
os.chdir(folder)


for path, subdirs, files in os.walk(folder):
    for name in files:
        if fnmatch(name, "*.TXT"):
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