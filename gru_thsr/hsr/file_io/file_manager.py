import os
from shutil import copyfile
from shutil import rmtree


def safely_remove_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)


def safely_remove_dir(dir_path):
    if os.path.exists(dir_path):
        rmtree(dir_path)


def refresh_dir(dir_path):
    safely_remove_dir(dir_path)
    os.mkdir(dir_path)


def safely_copy_file(source_file_name, destination_file_name):
    if os.path.isfile(source_file_name):
        copyfile(source_file_name, destination_file_name)
