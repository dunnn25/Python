import shutil
import os

def copy_func(des_dir, source_dir):
    list_name = os.listdir(des_dir)
    for file_name in list_name:
        shutil.copy(os.path.join(des_dir, file_name), os.path.join(source_dir,file_name))
    
source_dir = "Lesson 11 Function\source_dir"
des_dir = "Lesson 11 Function\des_dir"       
copy_func(des_dir,source_dir)

