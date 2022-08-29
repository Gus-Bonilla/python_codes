#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    Script to move files from diferent individual folders to the 
    main folder and rename them with their correspondant name.

    Author:             Gus-Bonilla
    Modification Date:  28/08/2022
"""


import os.path as pth
import os
import shutil as sht


def files_filter(elements_list, current_path, ext_to_look):
    # Function to filter elements in an iterable, by looking for all 
    # the files with the choossed file extention.
    
    filtered_files = list()

    for element in elements_list:
        if pth.isfile('{}{}'.format(current_path, element)):
            if element.endswith(ext_to_look):
                filtered_files.append(element)

    return filtered_files


def check_folder(folder_path, folders_list, files_list, ext_to_look):
    # Function to examine the content of a directory and and add its
    # content to its correspondant list.

    print('Checking folder:', folder_path)

    folder_content = os.listdir(folder_path)
    folders_in_folder = filter(pth.isdir, folder_content)
    files_in_folder = files_filter(folder_content,
                                  folder_path,
                                  ext_to_look)

    for folder in folders_in_folder:
        folders_list.append('{}{}/'.format(folder_path, folder))

    for file in files_in_folder:
        files_list.append('{}{}'.format(folder_path, file))
        

def main():
    # Main function

    ext_to_look = '.mkv'
    files_default_name_beg = 'Scissor Seven S1-C'
    files_default_name_end = ' [HD-1080P]'
    episode_number_idx = -29 # Index of the char with the episode number
    folders_list = list()
    files_list = list()
    folder_to_begin = './'
    destination_folder = './'

    folders_list.append(folder_to_begin)

    while len(folders_list):
        check_folder(folders_list.pop(), folders_list, files_list, ext_to_look)

    print('\n')

    for file in files_list:
        copy_counter = 2
        new_file_name = files_default_name_beg + file[episode_number_idx:episode_number_idx+2] + files_default_name_end
        file_lready_existent = pth.isfile(destination_folder + new_file_name + ext_to_look)

        if file == destination_folder+new_file_name+ext_to_look:
            continue

        while file_lready_existent:
            new_file_name = new_file_name + ' - {}'.format(copy_counter)

            if pth.isfile(destination_folder + new_file_name + ext_to_look):
                chars_to_remove = -4
                copy_counter_check = copy_counter

                while copy_counter_check > 10:
                    chars_to_remove -= 1
                    copy_counter_check = copy_counter_check / 10

                new_file_name = new_file_name[ : chars_to_remove]
                copy_counter += 1
            else:
                file_lready_existent = False

        print('\tMoving file: {}\n\n\t\tTo: {}{}{}\n'.format(file, destination_folder, new_file_name, ext_to_look))

        sht.move(file, destination_folder+new_file_name+ext_to_look, copy_function=sht.copy2)

    print('\n\tDONE :)')


if __name__ == "__main__":
    main()
