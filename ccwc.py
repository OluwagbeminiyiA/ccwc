import argparse
import os
import sys


def create_parser():
    parser = argparse.ArgumentParser(description='Command Line wc Tool')
    parser.add_argument("filename", metavar='FILE')
    parser.add_argument('-c', "--bytes", action="store_true", help='Print the byte counts')
    parser.add_argument('-l', "--lines", action="store_true", help='Print the newline counts')
    parser.add_argument('-w', "--words", action="store_true", help='Print the word counts')
    parser.add_argument('-m', "--chars", action="store_true", help='Print the character counts')
    return parser


def get_file_bytes(file_path):
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def get_file_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def get_file_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def get_file_chars(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            chars = len(content) + get_file_lines(file_path)
            return chars
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")


def calculate_all(file_path):
    return get_file_chars(file_path), get_file_words(file_path), get_file_lines(file_path), get_file_bytes(file_path)


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.bytes:
        print(get_file_bytes(args.filename))
    elif args.lines:
        print(get_file_lines(args.filename))
    elif args.words:
        print(get_file_words(args.filename))
    elif args.chars:
        print(get_file_chars(args.filename))
    elif len(sys.argv) == 2:
        print(calculate_all(args.filename))
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
