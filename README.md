# File Organizer (or choose a better name from our previous discussion!)

A Python script that automatically organizes files into folders based on their file extensions.

## Description

This script simplifies file management by automatically sorting files in a specified directory into organized folders. It categorizes files such as images, documents, software, and archives, creating a clean and structured file system. This helps to reduce clutter and improve workflow efficiency.

## Features

* **Automatic File Sorting:** Organizes files based on their extensions.
* **Customizable Folders:** Defines folder names and corresponding file extensions in a dictionary.
* **Directory Creation:** Automatically creates necessary folders if they don't exist.
* **Efficient File Movement:** Uses `shutil.move()` for fast and reliable file transfers.
* **Clear Output:** Prints messages indicating which files have been moved and where.

## Getting Started

### Prerequisites

* Python 3.x installed on your system.

### Installation

1.  Clone the repository to your local machine:

    ```bash
    git clone [your-repository-url]
    ```

2.  Navigate to the project directory:

    ```bash
    cd [project-directory]
    ```

### Usage

1.  **Modify the `source_folder` variable:** Open the Python script and change the `source_folder` variable to the path of the directory you want to organize.

    ```python
    source_folder = r"C:\Users\user\Downloads" # Example
    ```

2.  **Customize the `extension_map` dictionary (optional):** Modify the `extension_map` dictionary to add, remove, or change folder names and file extensions.

    ```python
    extension_map = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".xlsx", ".pptx"],
        # ... your custom mappings
    }
    ```

3.  **Run the script:**

    ```bash
    python your_script_name.py
    ```

    Replace `your_script_name.py` with the actual name of your Python file.

4.  The script will create folders (if needed) and move files accordingly, printing messages to the console.
