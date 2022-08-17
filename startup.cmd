@echo off
cd /d "%cd%/src" || exit
py main.py
cd ../
@echo on