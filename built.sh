#!/bin/bash
rm -rf dist build
pyinstaller --noconsole --onefile --icon="pomodoro-technique.ico" --name "MyPomodoro" --add-data="core:core" app.py
chmod +x dist/MyPomodoro
echo "Pronto! Seu botão novo está na pasta dist."