def get_version():
    return "1.0.0"

def validate_input(input_str):
    if not isinstance(input_str, str) or any(char in input_str for char in [';', '&', '|', '
]):
        raise ValueError("Invalid input detected")
    return input_str

if __name__ == "__main__":
    try:
        version = validate_input(get_version())
        print(version)
    except ValueError as e:
        print(f"Error: {e}")
