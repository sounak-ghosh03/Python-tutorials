# SHUTIL MODULE IN PYTHON

import shutil
import os

# shutil.copy("main.py", "main2.py")
# shutil.copytree(".tutorial", "mytutorial")
# shutil.move(".tutorial/file.file", "file.file")
# shutil.rmtree("mytutorial")
os.remove("file.file")


# Copying a file
shutil.copy("src.txt", "dst.txt")

# Copying a directory
shutil.copytree("src_dir", "dst_dir")

# Moving a file
shutil.move("src.txt", "dst.txt")

# Deleting a directory
shutil.rmtree("dir")
