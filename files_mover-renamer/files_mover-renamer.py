#!/usr/bin/env python3
# c-basic-offset: 4; tab-width: 8; indent-tabs-mode: nil
# vi: set shiftwidth=4 tabstop=8 expandtab:
# :indentSize=4:tabSize=8:noTabs=true:
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
    Script to move files from diferent individual folders to the 
    main folder and rename them with their correspondant name.
"""


import os.path as pth
import os
import shutil as sht


def custom_filter(filter_function, elements, current_folder_path):
    # Function to filter elements on an iterable based on a filter function
    
    filtered_elements = list()

    for element in elements:
        if pth.isfile('./{}/{}'.format(current_folder_path, element)):
            filtered_elements.append(element)

    return filtered_elements


def main():
    # Main function

    extension_to_look = '.mkv'
    files_default_name = 'Scissor Seven S1-CXX [HD-1080P]'
    episode_number_idx_src = 16
    episode_number_idx_dst = 18
    
    folders_list = os.listdir('.')
    folders_list = filter(pth.isdir, folders_list)

    for folder_name in folders_list:
        print('Checking folder:', folder_name)

        files_list = os.listdir('./{}/'.format(folder_name))
        files_list = custom_filter(pth.isfile, files_list, folder_name)

        for file_name in files_list:
            print('\tChecking file:', file_name)

            if file_name.endswith(extension_to_look):
                files_default_name = files_default_name[ : episode_number_idx_dst] + file_name[episode_number_idx_src : episode_number_idx_src+2] + files_default_name[episode_number_idx_dst+2 : ]
                
                print('\t\tMoving file as:', files_default_name+extension_to_look)

                sht.move('./{}/{}'.format(folder_name, file_name),
                            './{}{}'.format(files_default_name, extension_to_look),
                            copy_function=sht.copy2)

    print('\nDONE :)')


if __name__ == "__main__":
    main()
