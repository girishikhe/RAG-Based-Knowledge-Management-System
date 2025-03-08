import os
from pathlib import Path

# Define the folder structure and files in one list
project_structure = [
    "app/__init__.py",
    "app/config.py",
    "app/main.py",
    "app/models/__init__.py",
    "app/models/vector_store.py",
    "app/services/__init__.py",
    "app/services/llm_service.py",
    "app/static/style.css",
    "app/templates/index.html",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

# Create folders and files
for path in project_structure:
    filepath = Path(path)
    filedir, filename = os.path.split(filepath)

    # Create directories if they don't exist
    if filedir:
        os.makedirs(filedir, exist_ok=True)

    # Create empty files if they don’t exist
    if not filepath.exists():
        with open(filepath, "w") as f:
            pass  # Create an empty file
    else:
        print(f"File already exists: {filepath}")

print("Project structure created successfully!")
