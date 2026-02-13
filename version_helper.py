def get_version():
    """
    Returns the current version string.
    
    Returns:
        str: The version string in semantic versioning format.
    """
    version = "1.0.0"
    return version


if __name__ == "__main__":
    current_version = get_version()
    print(current_version)
