:: USED SOURCES
:: https://superuser.com/questions/62525/run-a-batch-file-in-a-completely-hidden-way
:: https://superuser.com/questions/1585731/run-a-bat-file-silently
:: https://stackoverflow.com/questions/507347/hide-command-window-of-bat-file-that-executes-another-exe-file
:: https://stackoverflow.com/questions/33685398/how-not-to-open-a-cmd-window-when-running-a-batch-file
:: https://www.reddit.com/r/Batch/comments/1d5z701/how_to_run_batch_hiddeninvisible/
:: https://www.tenforums.com/general-support/208200-can-i-run-batch-file-without-cmd-exe-window-popping-up.html
:: https://stackoverflow.com/questions/8678441/difference-between-wscript-and-cscript
:: https://serverfault.com/questions/38318/better-way-to-wait-a-few-seconds-in-a-bat-file
:: https://www.robvanderwoude.com/wait.php

@echo off

title JokeAPI

set VENV_NAME=jokeapi_venv

echo Starting JokeAPI server in the background...

set PYTHON_IN_VENV=%~dp0%VENV_NAME%\Scripts\python.exe

:: Create a VBScript file that runs the app.py file while in background and without printing
echo CreateObject("Wscript.Shell").Run """%PYTHON_IN_VENV%"" ""api/app.py"" ", 0, False > start_jokeapi_server.vbs

:: Run the newly created file
cscript //nologo start_jokeapi_server.vbs

del start_jokeapi_server.vbs

:: A small pause to ensure the server has started up fully
timeout /t 3 /nobreak >nul

echo Starting JokeAPI client...
echo.

:: Execute the user.py script which prompts a CLI window for the user to see.
"%PYTHON_IN_VENV%" user.py