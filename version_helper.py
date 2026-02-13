import re

def get_version():
    return "1.0.0"

def is_valid_version(version):
    return re.match(r'^\d+\.\d+\.\d+
, version) is not None

if __name__ == "__main__":
    version = get_version()
    if is_valid_version(version):
        print(version)
    else:
        print("Invalid version format")
