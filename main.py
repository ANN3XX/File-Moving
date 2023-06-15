import os
import shutil

def move_html_files(source_folder, destination_folder):
    # Get a list of all files in the source folder
    file_list = os.listdir(source_folder)
    
    # Filter the list to include only HTML files
    html_files = [file for file in file_list if file.endswith(".html")]
    
    # Move each HTML file to the destination folder
    for file in html_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.move(source_path, destination_path)
        print(f"Moved {file} to {destination_folder}")
    
    print("All HTML files have been moved.")

# Specify the source and destination folders
source_folder = "/path/to/source/folder"
destination_folder = "/path/to/destination/folder"

# Call the function to move the HTML files
move_html_files(source_folder, destination_folder)
