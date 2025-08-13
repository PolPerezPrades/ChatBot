@echo off
REM Name your environment
set ENV_NAME=.venv

REM Create the environment if it doesn't exist
if not exist %ENV_NAME% (
    echo Creating virtual environment...
    python -m venv %ENV_NAME%
) else (
    echo Virtual environment already exists.
)

REM Activate the environment
call %ENV_NAME%\Scripts\activate

REM Upgrade pip (optional but recommended)
python -m pip install --upgrade pip

REM Install packages (replace or add as needed)
pip install -r requirements.txt
ollama serve
ollama pull gemma3:4b

REM End of installations
echo Installations done.

REM Start the application
streamlit run src\main.py

