@echo off
cd /d "%~dp0"
python install.py --host codex %*
if errorlevel 1 pause
