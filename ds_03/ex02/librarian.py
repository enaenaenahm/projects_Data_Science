#!/usr/bin/env python3
import os
import subprocess
import sys

def check_virtual_env():
    venv = os.environ.get("VIRTUAL_ENV")
    if not venv:
        raise EnvironmentError("Not running inside a virtual environment.")
    if not os.path.basename(venv) == "enahm_env":
        raise EnvironmentError(f"Wrong virtual environment: {venv}")
    return venv

def install_requirements():
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)

def save_installed_packages():
    with open("requirements.txt", "w") as f:
        subprocess.run([sys.executable, "-m", "pip", "freeze"], stdout=f, check=True)

def display_installed_packages():
    subprocess.run([sys.executable, "-m", "pip", "freeze"])

def main():
    try:
        check_virtual_env()
        install_requirements()
        save_installed_packages()
        display_installed_packages()
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
