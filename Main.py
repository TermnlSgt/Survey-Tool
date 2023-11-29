import os 
import tkinter as tk
from tkinter.filedialog import askdirectory

def move_file():

    # Allows user to select raw and processed directories
    raw_folder = askdirectory(title = 'Select Raw Line Folder')
    processed_folder = askdirectory(title = 'Select Processed Folder')

    # Places files from user defined directories in list
    raw_dir = os.listdir(raw_folder)
    processed_dir = os.listdir(processed_folder)

    # Compairs lists to see if any new files have entered directory
    new_file = [item for item in raw_dir if item not in processed_dir]

    # Combines folder and document to create one complete path also titles new document 
    new_raw_file_path = f'{raw_folder}/{str(*new_file)}'
    new_processed_file_path = f'{processed_folder}/{str(*new_file)}'

    # Imports  variables and calls list_dir() function
    new_raw_file_path, new_processed_file_path = list_dir()

    # Moves File
    with open(new_raw_file_path, 'r') as raw, open(new_processed_file_path, 'w') as processed:
        for line in raw:
            processed.write(line)

move_file()