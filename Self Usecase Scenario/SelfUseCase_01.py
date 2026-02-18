# Renaming the multiple files in directory by adding prefix/suffix to it.

import os
directory=input()
prefix=input()
suffix=input()

for file in os.listdir(directory):
    oldPath=os.path.join(directory,file)
    name,extension=os.path.splitext(file)
    new_file=f"{prefix}{name}{suffix}{extension}"
    newPath=os.path.join(directory,new_file)
    os.rename(oldPath,newPath)
