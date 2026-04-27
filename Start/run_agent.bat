@echo off
title AI Agent Dashboard
color 0b
echo ==================================================
echo   ANTIGRAVITY - G4F PC AUTONOMOUS AGENT DASHBOARD
echo ==================================================
echo.
echo Dang khoi dong Agent...
echo.

:: Di chuyen ve thu muc cha (D:\Use Computer\)
cd /d "%~dp0.."

if exist ".\.venv\Scripts\python.exe" (
    echo [INFO] Dang dung moi truong ao .venv
    ".\.venv\Scripts\python.exe" main.py
) else (
    echo [INFO] Dang dung Python he thong
    python main.py
)
pause