#!/usr/bin/env python3
import os

def print_virtual_env():
    try:
        venv = os.getenv("VIRTUAL_ENV") or (_ for _ in ()).throw(EnvironmentError("No virtual environment is currently active."))
        print(f"Your current virtual env is {venv}")
    except Exception as e:
        print(f"{e}")

if __name__ == '__main__':
    print_virtual_env()
