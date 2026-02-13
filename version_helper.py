def get_version():
    return "1.0.0"

if __name__ == "__main__":
    version = get_version()
    if isinstance(version, str) and version.isalnum():
        print(version)
    else:
        print("Invalid version format")
