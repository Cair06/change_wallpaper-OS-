import struct
import ctypes
import random 
from os import listdir, getcwd
from os.path import isfile, join

mypath = join(getcwd(),'img')
all_files_in_dir = [f for f in listdir(mypath) if isfile(join(mypath, f))]
all_files_with_path=[]

for i in all_files_in_dir:
	all_files_with_path.append(join(mypath, i))

def changeBG(path):
	SPI_SETDESKWALLPAPER = 20
	ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, random.choice(path), 3)

changeBG(all_files_with_path)
