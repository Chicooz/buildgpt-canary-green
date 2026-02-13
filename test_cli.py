import subprocess


def test_dry_run_flag():
    result = subprocess.run(['python', 'cli.py', '--dry-run'], capture_output=True, text=True)
    assert 'Dry run: No actions will be executed' in result.stdout


def test_no_flag():
    result = subprocess.run(['python', 'cli.py'], capture_output=True, text=True)
    assert 'Executing actions...' in result.stdout
