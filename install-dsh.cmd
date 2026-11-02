@echo off
cd /d "%~dp0"
python install.py --host dsh %*
if errorlevel 1 pause
