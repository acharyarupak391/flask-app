import subprocess

subprocess.Popen(["gunicorn", "--bind", "0.0.0.0:3000", "run:app"])
