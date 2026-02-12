from urllib.parse import urlparse

def is_valid_url(url: str) -> bool:
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

if __name__ == "__main__":
    test_url = input("Enter a URL to validate: ")
    print("Valid URL" if is_valid_url(test_url) else "Invalid URL")
