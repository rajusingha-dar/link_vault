import os
import pathlib

def create_project_structure():
    """
    Creates the directory and file structure for the Link Saver application.
    """
    # Define the project's root directory name
    root_dir = "link-saver-app"
    
    # Define the directory structure
    directories = [
        os.path.join(root_dir, "app", "static", "css"),
        os.path.join(root_dir, "app", "static", "js"),
        os.path.join(root_dir, "app", "templates"),
    ]

    # Define the list of empty files to be created
    files = [
        os.path.join(root_dir, "requirements.txt"),
        os.path.join(root_dir, ".gitignore"),
        os.path.join(root_dir, "README.md"),
        os.path.join(root_dir, ".env"),
        os.path.join(root_dir, "app", "__init__.py"),
        os.path.join(root_dir, "app", "main.py"),
        os.path.join(root_dir, "app", "crud.py"),
        os.path.join(root_dir, "app", "models.py"),
        os.path.join(root_dir, "app", "schemas.py"),
        os.path.join(root_dir, "app", "database.py"),
        os.path.join(root_dir, "app", "templates", "index.html"),
        os.path.join(root_dir, "app", "static", "css", "styles.css"),
        os.path.join(root_dir, "app", "static", "js", "script.js"),
    ]
    
    print(f"Creating project structure for '{root_dir}'...")

    # Create the root directory if it doesn't exist
    os.makedirs(root_dir, exist_ok=True)

    # Create sub-directories
    for dir_path in directories:
        try:
            os.makedirs(dir_path, exist_ok=True)
            print(f"  Created directory: {dir_path}")
        except OSError as e:
            print(f"Error creating directory {dir_path}: {e}")

    # Create empty files
    for file_path in files:
        try:
            pathlib.Path(file_path).touch()
            print(f"  Created file: {file_path}")
        except IOError as e:
            print(f"Error creating file {file_path}: {e}")

    # Add this setup script to the root directory as well
    pathlib.Path(os.path.join(root_dir, "setup.py")).touch()

    print("\nProject structure created successfully!")
    print(f"Navigate into your project folder with: cd {root_dir}")
    print("Next, create a virtual environment and install dependencies from requirements.txt.")

if __name__ == "__main__":
    create_project_structure()
