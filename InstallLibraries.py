import subprocess
import sys
import os

def InstallColorama():
    try:
        import colorama
    except ImportError:
        print("colorama not found. Installing...")
        WheelPath = os.path.join(os.path.dirname(__file__), 'Libraries', 'colorama-0.4.6-py2.py3-none-any.whl')
        if not os.path.exists(WheelPath):
            raise FileNotFoundError(f"'{WheelPath}' not found.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", WheelPath])