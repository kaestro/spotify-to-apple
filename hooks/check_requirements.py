# hooks/check_requirements.py
import os
import subprocess
import sys


def main():
    # Determine the correct command to use based on the operating system
    if os.name == "nt":
        pip_command = ["venv\\Scripts\\python", "-m", "pip", "freeze"]
    else:
        pip_command = ["venv/bin/python", "-m", "pip", "freeze"]

    # Get the current requirements
    current_requirements = subprocess.run(
        pip_command, capture_output=True, text=True, check=True
    ).stdout

    # Read the requirements.txt file
    with open("requirements.txt", "r", encoding="utf-16") as f:
        file_requirements = f.read()

    # Compare the current requirements with the requirements.txt file
    if current_requirements != file_requirements:
        print(
            "requirements.txt is out of date. Please update it and commit the changes."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
