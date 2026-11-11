# DSA AI Tutor

A command-line Data Structures and Algorithms tutor powered by the Gemini API.

## Setup on Windows

From this project folder, run these commands in PowerShell:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set `GEMINI_API_KEY` to a key from Google AI
Studio. Keep `.env` private; it is excluded by `.gitignore`.

Run the tutor and, optionally, list models available to the configured key:

```powershell
python main.py
python check_models.py
```

Python 3.12 is the tested version for this practical. If it is unavailable,
replace `3.12` with an installed Python version supported by the dependencies.
