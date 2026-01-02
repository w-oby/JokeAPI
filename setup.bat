:: USED SOURCES
:: https://docs.python.org/3/library/venv.html
:: https://docs.python-guide.org/dev/virtualenvs/
:: https://superuser.com/questions/1547228/how-to-activate-python-virtualenv-through-shell-script
:: https://www.tutorialspoint.com/batch_script/batch_script_variables.htm
:: https://www.reddit.com/r/sysadmin/comments/106k3ec/batch_script_cmd_how_to_set_variable_into_another/
:: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1
:: https://forums.tomshardware.com/threads/windows-batch-file-set-output-of-program-to-a-variable.996281/
:: https://www.tutorialspoint.com/batch_script/batch_script_if_else_statement.htm
:: https://stackoverflow.com/questions/4340350/how-to-check-if-a-file-exists-from-inside-a-batch-file
:: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/if
:: https://stackoverflow.com/questions/1164049/batch-files-error-handling
:: https://stackoverflow.com/questions/42808223/error-handling-in-bat-file
:: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/pause
:: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/exit
:: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/goto
:: https://superuser.com/questions/1643414/confused-about-goto-label-batch-file-windows
:: https://www.computerhope.com/goto.htm


@echo off

title JokeAPI Setup

:: Setting a fixed value for the virtual environment, so it won't be mistaken with any other existing venv's.
set VENV_NAME=jokeapi_venv

echo    =======================================================
echo.
echo.
echo    Welcome to the JokeAPI Setup!
echo.
echo    This script will create the virtual environment (%VENV_NAME%)
echo    and install the required packages from requirements.txt.
echo.
echo.
echo    =======================================================
echo.

pause

:: Checking if map exists
if EXIST %VENV_NAME% (

    echo Virtual environment '%VENV_NAME%' already exists.

) else (

    echo Creating virtual environment...

    :: Creating a Python virtual environment in root dir
    python -m venv %VENV_NAME%

)

:: Error handling if above code block failed. Basically if not 0 (success/OK), then go to error_handling
if %errorlevel% NEQ 0 goto error_handling

echo.
echo Installing required packages...
echo.

:: Installing packages. Python.exe -m ensures that packages will still install, even if you don't have pip installed.
.\%VENV_NAME%\Scripts\python.exe -m pip install -r requirements.txt

:: Error handling if above code block failed. If not 0 (success or OK), then go to error_handling
if %errorlevel% NEQ 0 goto error_handling

:: Success if above code block executed
goto success

:: This occurs when any of the code blocks above have not executed successfully.
:error_handling

echo.
echo    ===================== ERROR =========================
echo.
echo.
echo    An error occurred during setup.
echo.
echo    Please check the following requirements are satisfied:
echo        - Python is installed and available from the CLI or terminal.
echo        - You have a working internet connection.
echo        - The 'requirements.txt' file has not been changed or corrupted.
echo.
echo.
echo    =======================================================
echo.

pause
exit /b 1

:: This part occurs when all of the code blocks have been executed successfully and is next on the flow of code execution.
:success

echo.
echo    ==================== SUCCESS ========================
echo.
echo.
echo    Setup has been completed!
echo.
echo    You can now run the application by 
echo    double-clicking on 'start_app.bat'.
echo.
echo.
echo    =======================================================
echo.

pause
exit /b 0