import os
import shutil
import logging 

folder = input("Enter folder path : ")

if os.path.isdir(folder):
    print("Folder Found")
else:
    print("Folder Not Found")

files = os.listdir(folder)
for file in files:
    print(file)