import argparse


def main():
    parser = argparse.ArgumentParser(description='CLI for buildgpt-canary-green')
    parser.add_argument('--dry-run', action='store_true', help='Print actions without executing them')
    args = parser.parse_args()

    if args.dry_run:
        print('Dry run: No actions will be executed.')
    else:
        print('Executing actions...')


if __name__ == '__main__':
    main()
