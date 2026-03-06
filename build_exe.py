"""
Build script to create standalone executable for CPU Optimizer Pro
This script uses PyInstaller to create a Windows executable
"""

import os
import sys
import subprocess
import shutil

def build_executable():
    """Build standalone executable using PyInstaller"""
    
    print("=" * 60)
    print("CPU Optimizer Pro - Executable Builder")
    print("=" * 60)
    print()
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
        print("[OK] PyInstaller is installed")
    except ImportError:
        print("[*] PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        print("[OK] PyInstaller installed successfully")
    
    print()
    print("Building executable...")
    print()
    
    # PyInstaller command with options
    build_command = [
        "pyinstaller",
        "--name=CPUOptimizerPro",
        "--onefile",  # Single executable file
        "--noconsole",  # No console window (changed from --windowed)
        "--noupx",  # Disable UPX compression for compatibility
        "--clean",  # Clean cache before building
        "--hidden-import=psutil",
        "--collect-submodules=psutil",
        "--collect-binaries=psutil",
        "--hidden-import=matplotlib",
        "--hidden-import=matplotlib.backends.backend_tkagg",
        "--hidden-import=numpy",
        "--hidden-import=PIL",
        "--hidden-import=tkinter",
        "--collect-all=matplotlib",
        "--collect-all=psutil",
        "CPUOptimizer.py"
    ]
    
    # Run PyInstaller
    try:
        subprocess.check_call(build_command)
        print()
        print("=" * 60)
        print("[OK] Build completed successfully!")
        print("=" * 60)
        print()
        print("Executable location: dist\\CPUOptimizerPro.exe")
        print("Size: ~50-80 MB (includes Python runtime and all libraries)")
        print()
        print("You can now:")
        print("1. Test the executable: dist\\CPUOptimizerPro.exe")
        print("2. Create an installer using build_installer.iss")
        print("3. Distribute the installer to users")
        print()
        
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Build failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    build_executable()
