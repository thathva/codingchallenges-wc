import argparse
import sys

def word_stream(file, delim):
    """Generator that yields words from the file based on the given delimiter."""
    for line in file:
        for word in line.split(delim):
            if word:
                yield word.strip()

def word_count(file):
    """Counts and returns the number of words in the file."""
    word_count = sum(1 for _ in word_stream(file, " "))
    

def byte_count(file):
    """Counts and returns the total number of bytes in the file."""
    return sum(len(word.encode('utf-8')) for word in word_stream(file, " "))

def line_count(file):
    """Counts and returns the number of lines in the file."""
    return sum(1 for _ in file)

def char_count(file):
    """Counts and returns the total number of characters in the file."""
    return sum(len(word) for word in word_stream(file, " "))

def default(file):
    """Counts lines, words, bytes, and characters in a single pass."""
    line_count = 0
    word_count = 0
    byte_count = 0
    char_count = 0

    for line in file:
        line_count += 1
        words = line.split()
        word_count += len(words)
        byte_count += len(line.encode('utf-8'))
        char_count += len(line)

    return line_count, word_count, byte_count, char_count

def main():
    parser = argparse.ArgumentParser(description="WC Tool")

    parser.add_argument("-l", "--lines", action='store_true', help="Line Count")
    parser.add_argument("-c", "--bytes", action='store_true', help="Byte Count")
    parser.add_argument("-w", "--words", action='store_true', help="Word Count")
    parser.add_argument("-m", "--chars", action='store_true', help="Char Count")

    parser.add_argument('filename', nargs='?', type=str, help='Name of the file to process')

    args = parser.parse_args()

    if args.filename:
        # Reading from the specified file
        try:
            open_file = open(args.filename, "r", encoding='utf-8')
        except FileNotFoundError:
            print(f"Error: File '{args.filename}' not found.")
            return
    else:
        # Reading from stdin
        open_file = sys.stdin
        
    if args.lines:
        print("Line Count:", line_count(open_file))
    elif args.bytes:
        print("Byte Count:", byte_count(open_file))
    elif args.words:
        print("Word Count:", word_count(open_file))
    elif args.chars:
        print("Character Count:", char_count(open_file))
    else:
        print("Line Count:", default(open_file))
    if args.filename:
        open_file.close()

if __name__ == '__main__':
    main()
