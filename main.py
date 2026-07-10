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
    path = os.path.join(folder,file)
    
    if os.path.isfile(path):
        
        extension = os.path.splitext(file)[1].lower()
        print(file,extension)
    
categories = {
    "Images" : [".jpg",".jpeg",".png",".gif"],
    "Documents" : [".pdf",".doc",".docx",".txt"],
    "Videos" : [".mp4", ".mkv",".avi"],
    "Music" : [".mp3",".wav"],
    "Programs" : [".exe",".msi"],
    "Archives" : [".zip",".rar",".7z"]
}

