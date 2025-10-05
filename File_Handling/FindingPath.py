
import os
for dirpath,dirnames,filenames in os.walk('.'):
    print("current directory path",dirpath)
    print("directories",dirnames)
    print("files",filenames)
    print()