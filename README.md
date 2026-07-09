# Python Automation Script

## Overview

The File Organizer Automation Script is a Python application that automatically organizes files in a selected folder based on their file extensions. It helps keep directories clean by sorting files into categories such as Images, Documents, Music, Videos, Archives, and Others.

The project also generates a log file to record every operation and uses exception handling to manage errors without crashing.

---

## Features

* Organizes files automatically based on file extension.
* Creates category folders if they do not already exist.
* Moves files into their respective folders.
* Generates a log file (`operations.log`) for all operations.
* Accepts folder path as user input.
* Uses exception handling for error management.
* Supports multiple common file types.

---

## Technologies Used

* Python 3
* OS Module
* Shutil Module
* Logging Module

---

## Project Structure

```text
Pyhton Automation Script/
│
├── main.py
├── operations.log
├── README.md
└── TestFolder/
```

---

## Supported File Categories

| Category  | Extensions                |
| --------- | ------------------------- |
| Images    | .jpg, .jpeg, .png, .gif   |
| Documents | .pdf, .doc, .docx, .txt   |
| Music     | .mp3, .wav                |
| Videos    | .mp4, .mkv, .avi          |
| Archives  | .zip, .rar, .7z           |
| Others    | Any unsupported file type |

---

## How It Works

1. The user enters the folder path.
2. The program checks whether the folder exists.
3. All files in the folder are scanned.
4. The extension of each file is identified.
5. A destination folder is selected based on the extension.
6. If the destination folder does not exist, it is created automatically.
7. The file is moved to the appropriate folder.
8. Every operation is recorded in `operations.log`.
9. Any errors encountered are handled using exception handling.

---

## Example

### Before

```text
TestFolder/
│
├── photo.jpg
├── report.pdf
├── song.mp3
├── movie.mp4
├── notes.txt
├── data.xyz
```

### After

```text
TestFolder/
│
├── Images/
│   └── photo.jpg
│
├── Documents/
│   ├── report.pdf
│   └── notes.txt
│
├── Music/
│   └── song.mp3
│
├── Videos/
│   └── movie.mp4
│
└── Others/
    └── data.xyz
```

---

## Sample Console Output Shows

```text
Enter folder path:
D:\TestFolder

Files organized successfully.
Check operations.log for details.
```

---

## In Sample Log File You See

```text
2026-07-09 18:30:21 - photo.jpg moved to Images
2026-07-09 18:30:21 - report.pdf moved to Documents
2026-07-09 18:30:22 - song.mp3 moved to Music
2026-07-09 18:30:22 - movie.mp4 moved to Videos
```

---

## Requirements

* Python 3.x
* No external libraries are required.

---

## How to Run

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the project folder.

```bash
cd Python Automation Script
```

3. Run the program.

```bash
python main.py
```

4. Enter the folder path when prompted.

---

## Future Improvements

* Automatic file renaming.
* Duplicate file detection.
* Sort files by creation or modification date.
* Graphical User Interface (GUI).
* Drag-and-drop folder support.
* Undo last organization operation.

---

## Learning Outcomes

Through this project, you will learn:

* Working with the `os` module.
* File and directory handling in Python.
* Moving files using the `shutil` module.
* Logging operations using the `logging` module.
* Exception handling.
* User input handling.
* Building a simple automation application.

---

## License

This project is developed for educational purposes and can be modified or extended for personal learning.
