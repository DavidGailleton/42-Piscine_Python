import site
import os
import sys


def not_in_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment: None detected\n")
    print("WARNING: You're in the global environment!\n\
The machines can see everything you install.\n")
    print("To enter the construct, run:\n\
python -m venv matrix_env\n\
source matrix_env/bin/activate # On Unix\n\
matrix_env\n\
Scripts\n\
activate # On Windows\n")
    print("Then run this program again.")


def in_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")
    print(f"Current Python: {sys.executable}")
    print(f"Virtual Environment: {sys.prefix.split('/')[-1]}")
    print(f"Environment Path: {sys.prefix}")
    print("\nSUCCESS: You're in an isolated environment!\n\
Safe to install packages without affecting\n\
the global system.\n")
    print("Package installation path:")
    print(site.getsitepackages()[0])


def main() -> None:
    if "VIRTUAL_ENV" in os.environ:
        in_venv()
    else:
        not_in_venv()


if __name__ == "__main__":
    main()
