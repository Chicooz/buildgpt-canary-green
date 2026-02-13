import argparse

def get_version():
    return "1.0.0"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Version Helper')
    parser.add_argument('--dry-run', action='store_true', help='Print what would happen without executing')
    args = parser.parse_args()
    if args.dry_run:
        print('Dry run: would print version')
    else:
        print(get_version())
