# Python Workspace

A simple Python workspace with VS Code configuration.

## Files

- `main.py` — sample entrypoint
- `requirements.txt` — dependency list
- `.vscode/launch.json` — debug configuration
- `.vscode/tasks.json` — run task configuration

## Getting Started

1. Open this folder in VS Code.
2. Install the Python extension if prompted.
3. Select a Python interpreter: `Ctrl+Shift+P` → `Python: Select Interpreter`.
4. Run `main.py` using the green run button or press `F5`.

## Virtual Environment

Create a virtual environment if desired:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```
