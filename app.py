import subprocess

subprocess.Popen(["gunicorn", "--bind", "0.0.0.0:8080", "run:app"])