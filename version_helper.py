def get_version():
    """Return the current version string."""
    version = "1.0.0"
    return version


def main():
    """Print the current version when run as a script."""
    current_version = get_version()
    print(current_version)


if __name__ == "__main__":
    main()
