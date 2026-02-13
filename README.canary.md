# buildgpt-canary-green

Minimal always-green repo for CodeOps merge canary tests.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/buildgpt-canary-green.git
   cd buildgpt-canary-green
   ```

2. Ensure you have Python installed (version 3.6 or higher).

3. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install any necessary dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To check the version of the application, run:
```bash
python version_helper.py
```

This will output the current version of the application.