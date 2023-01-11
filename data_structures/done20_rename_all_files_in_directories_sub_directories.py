"""
rename folder and sub-folder and files and subfiles

"""

import os

def rename_folder_subfolders_and_files(path):
    try:
        print("path of the director is: ", path)
        count = 5
        for root, dirs, files in os.walk(path):
            for file in files:
                print(type(file))
                os.rename(os.path.join(root, file), os.path.join(root, file + str(count)))
                count += 1
    except Exception as err:
        print("Exception is \n", str(err))




# path = "/Users/vishal.g/PycharmProjects/pythonProject/data_structures/rename_folder"
# cur_working_dir = os.getcwd() + "/rename_folder"

cur_working_dir = os.path.join(os.path.abspath('.'), 'rename_folder')
# print(cur_working_dir)
# print(type(cur_working_dir))


rename_folder_subfolders_and_files(cur_working_dir)
