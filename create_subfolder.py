import os
import shutil
import pandas as pd

# set the path to the folder with subfolders
original_folder_path = "D:\DDSM\manifest-ZkhPvrLo5216730872708713142\CBIS-DDSM"

# set the path to the CSV file with folder entries
csv_file_path = "D:\DDSM\manifest-ZkhPvrLo5216730872708713142\metadata.csv"

# set the path to the new folder that will contain the filtered subfolders
new_folder_path = "D:\DDSM\manifest-ZkhPvrLo5216730872708713142\subfolder-ddsm"

# set the number of top entries to filter
num_top_entries = 3000

# read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# replace 'subfolder-ddsm' with the actual subfolder name that contains the subfolders you want to filter
df_filtered = df[df['Subject ID'].str.startswith('Calc-','Mass-')]

# sort the filtered DataFrame by the 'Number of Entries' column in descending order
df_sorted = df_filtered.sort_values(by=['Subject ID'], ascending=False)

# filter the top entries
df_top = df_sorted.head(num_top_entries)

# create the new folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.mkdir(new_folder_path)

# loop through the index values of the top entries and copy the corresponding subfolders to the new folder
for index in df_top.index:
    subfolder_name = df_top.loc[index, 'Subject ID']
    subfolder_path = os.path.join(original_folder_path, subfolder_name)
    new_subfolder_path = os.path.join(new_folder_path, subfolder_name)
    if os.path.isdir(subfolder_path) and not os.path.exists(new_subfolder_path):
        shutil.copytree(subfolder_path, new_subfolder_path)

print("Top 3000 subfolders with most entries copied to:", new_folder_path)


