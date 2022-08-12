@echo off
cd /d "%cd%/src" || exit
py main.py || exit
cd ../
@echo on