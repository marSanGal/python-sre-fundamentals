import subprocess, sys

def test_script_runs():
    proc = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
    assert proc.returncode == 0
    assert "fundamentals" in proc.stdout.lower() or "hello" in proc.stdout.lower()
