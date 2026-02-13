# buildgpt-canary-green

Minimal always-green repo for CodeOps merge canary tests.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Chicooz/buildgpt-canary-green.git
   cd buildgpt-canary-green
   ```

2. Ensure you have Python installed (version 3.6 or higher).

3. Run the version helper script to verify setup:
   ```bash
   python version_helper.py
   ```

## Usage Example

To see the always-green CI in action, push any changes to a branch or open a pull request. The GitHub Actions workflow will run and always pass, demonstrating the canary test setup.
