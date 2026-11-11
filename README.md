# DSA AI Tutor

A command-line Data Structures and Algorithms tutor powered by the Gemini API.

## Setup on Windows

From this project folder, run these commands in PowerShell:

```powershell
py --list
py -3.12 --version
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

If PowerShell blocks activation, allow it for the current terminal only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

After activation, use `python -m pip` so package commands target the active
virtual environment. Installing `-r requirements.txt` installs both
`google-genai` and `python-dotenv`.

If `py -3.12 --version` reports that no suitable runtime is installed, install
Python 3.12 first or substitute a version shown by `py --list` in the commands
above. If a virtual environment is already active, check it with
`python --version`; do not recreate it just to install packages.

Copy `.env.example` to `.env` and set `GEMINI_API_KEY` to a key from Google AI
Studio. Keep `.env` private; it is excluded by `.gitignore`.

Run the tutor and, optionally, list models available to the configured key:

```powershell
python main.py
python check_models.py
```

If you add or change dependencies and need to regenerate the lock list in
PowerShell, use:

```powershell
python -m pip freeze | Out-File -Encoding ascii requirements.txt
```

Keep a space before `>` if using `python -m pip freeze > requirements.txt`;
without it, PowerShell can pass `freeze>requirements.txt` to pip as an argument.

Python 3.12 is the tested version for this practical. If it is unavailable,
replace `3.12` with an installed Python version supported by the dependencies.
