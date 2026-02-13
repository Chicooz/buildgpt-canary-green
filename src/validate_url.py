import re

def is_valid_url(url: str) -> bool:
    # Simple regex for URL validation
    url_regex = re.compile(
        r'^(https?:\/\/)?'  # http:// or https://
        r'((([a-z\d]([a-z\d-]*[a-z\d])*)\.)+[a-z]{2,}|'  # domain...
        r'((\d{1,3}\.){3}\d{1,3}))'  # ...or ipv4
        r'(\:\d+)?(\/[-a-z\d%_.~+]*)*'  # optional port and path
        r'(\?[;&a-z\d%_.~+=-]*)?'  # query string
        r'(\#[-a-z\d_]*)?$', re.IGNORECASE)  # fragment locator
    return re.match(url_regex, url) is not None
