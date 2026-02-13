import re


def is_valid_url(url: str) -> bool:
    # Simple regex for URL validation
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?))'  # domain...
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(url_regex, url) is not None
