import os

folder_path = "" # copy the path ~
file_list = [f for f in os.listditr(folder_path) if not f.startswith('.') and f.endswith('.txt')]
# to filter the file list 
# also if you are not renaming files that end with .txt you have to change the .endswith as well

for index, filename in enumerate(file_list):
    if filename.startswith('.'): # this is to skip the ghost files in mac
        continue

    name, ext = os.path.splitext(filename) 
    # to split the extension and name
    # i.g. test.txt -> test and .txt

    old = os.path.join(folder_path, filename)
    # this joins the folder path and file name together so computer don't get confused

    new_name = f"n_{index}{ext}" # here to change the new file name desired
    new = os.path.join(folder_path, new_name) # see the os.path.join too, also don't swap the position, path comes first

    print(f"Renaming {filename} to {new_name} ...") # just for clarity ~

    os.rename(old, new)