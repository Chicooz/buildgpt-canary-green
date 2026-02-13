import subprocess
import sys

def test_version_output():
    result = subprocess.run([sys.executable, 'version_helper.py'], capture_output=True, text=True)
    assert result.stdout.strip() == '1.0.0'

def test_dry_run_output():
    result = subprocess.run([sys.executable, 'version_helper.py', '--dry-run'], capture_output=True, text=True)
    assert result.stdout.strip() == 'Dry run: would print version'
