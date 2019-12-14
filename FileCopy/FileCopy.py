import os
import shutil

def my_copy_func(src, dst):
    print("Sorce:" + src + ", Destination:" + dst)

    items = os.listdir(src)

    if not os.path.exists(dst):
        os.mkdir(dst)
    
    for item in items:
        srcFullPath = os.path.join(src, item)

        if os.path.isdir(srcFullPath):
            destFullPath = os.path.join(dst, item)
            print("This is directory:", srcFullPath)
            my_copy_func(srcFullPath, destFullPath)
        else:
            print("This is file:", srcFullPath)
            shutil.copy2(srcFullPath, dst)

curWorkingDir = os.getcwd()
srcPath = os.path.join(curWorkingDir, "experiment\src")
destPath = os.path.join(curWorkingDir, "experiment\dest")

my_copy_func(srcPath, destPath)

print("complete")
