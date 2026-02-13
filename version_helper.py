def get_version():
    return "1.0.0"

def is_valid_version(version):
    return isinstance(version, str) and version.count('.') == 2 and all(part.isdigit() for part in version.split('.'))

if __name__ == "__main__":
    version = get_version()
    if is_valid_version(version):
        print(version)
    else:
        print("Invalid version format")
