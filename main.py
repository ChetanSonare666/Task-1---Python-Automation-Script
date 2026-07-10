import os
import shutil
import logging

# Logging Configuration
logging.basicConfig(
    filename="operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# File Categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".exe", ".msi"],
    "Archives": [".zip", ".rar", ".7z"]
}

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist.")
    exit()

try:
    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1].lower()

            moved = False

            for category, extensions in categories.items():

                if extension in extensions:

                    destination = os.path.join(folder_path, category)

                    os.makedirs(destination, exist_ok=True)

                    shutil.move(file_path, os.path.join(destination, file))

                    logging.info(f"Moved {file} -> {category}")

                    moved = True
                    break

            if not moved:

                others = os.path.join(folder_path, "Others")

                os.makedirs(others, exist_ok=True)

                shutil.move(file_path, os.path.join(others, file))

                logging.info(f"Moved {file} -> Others")

    print("Organization Completed Successfully!")

except Exception as e:

    logging.error(str(e))

    print("Error:", e)