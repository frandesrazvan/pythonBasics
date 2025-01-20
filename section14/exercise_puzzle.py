import shutil
import os
import re

shutil.unpack_archive('unzip_me_for_instructions.zip', 'instructions', 'zip')
search_file = 'C:\\Users\\RFRANDES\\Downloads\\automation repo\\python\\TheCompletePythonBootcampFromZeroToHeroInPython\\section14\\instructions'
for folder, sub_folders, files in os.walk(search_file):
    # Iterate through the files in the folder
    for f in files:
        file_path = os.path.join(folder, f)  # Combine folder path and file name
        with open(file_path, 'r') as file:
            for line in file:
                pattern = r'\d{3}-\d{3}-\d{4}'
                match = re.search(pattern, line)

                if match:
                    print(match[0])
        file.close()
