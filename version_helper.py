def get_version():
    return "1.0.0"

def get_optional_config(config=None):
    if config is None:
        return {}
    return config

if __name__ == "__main__":
    print(get_version())
    # Test for null pointer crash fix
    assert get_optional_config() == {}, "Failed: get_optional_config() should return an empty dict when config is None"
    assert get_optional_config({"key": "value"}) == {"key": "value"}, "Failed: get_optional_config() should return the provided config"
