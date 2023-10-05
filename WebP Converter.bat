@echo off
setlocal enabledelayedexpansion

REM Loop through all selected files
for %%A in (%*) do (
   REM Get the full path of the input file
   set "input_file=%%~dpA%%~nxA"

   REM Get the directory of the input file
   set "input_dir=%%~dpA"

   REM Remove trailing backslash from input_dir
   if "!input_dir:~-1!"=="\" set "input_dir=!input_dir:~0,-1!"

   REM Convert the input file to webp in the same directory
   start /min python "C:\WebP Converter\convert_to_webp.py" "!input_file!" "!input_dir!"
)
