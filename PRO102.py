import sys
import os
import shutil


from_dir = "C:/Users/vidhi/OneDrive/Documents/Coding/Python/C102/Image_Files"
to_dir = "C:/Users/vidhi/Downloads"

listFiles = os.listdir(from_dir)
print(listFiles)

for file_name in listFiles:

    name, extension = os.path.splitext(file_name)
    print("NAME OF FILE: ",name)
    print("EXTENSION: ", extension)

    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpeg', '.jpg','.webp','.jfif' ]:
        
        # The code block you provided is creating three paths:
        path1 = from_dir + '/' + file_name                              # Example path1 : C:/Users/vidhi/Downloads/image1.png      
        path2 = to_dir + '/' + "Image_Files"                     # Example path2 : C:/Users/vidhi/OneDrive/Desktop/Image_Files      
        path3 = to_dir + '/' + "Image_Files" + '/' + file_name   # Example path3 : C:/Users/vidhi/OneDrive/Desktop/Image_Files/image1.jpg
        print("path1:  " , path1)
        print("path2:  ", path2)
        print("path3:  ", path3)

        if os.path.exists(path2):
          print("Moving " + file_name + ".....")
          shutil.move(path1, path3)

        else:
          os.makedirs(path2)
          shutil.move(path1, path3)

