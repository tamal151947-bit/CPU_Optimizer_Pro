@echo off
echo ========================================
echo CPU Optimizer Pro - Installation Script
echo ========================================
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)
echo.

echo Installing required dependencies...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation completed successfully!
echo ========================================
echo.
echo You can now run CPU Optimizer Pro by:
echo 1. Double-clicking CPUOptimizer.py
echo 2. Or running: python CPUOptimizer.py
echo.
echo For best results, run as Administrator!
echo.
pause
