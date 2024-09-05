
---

# Command Line `wc` Tool

A simple Python command-line tool that mimics the behavior of the Unix `wc` (word count) command. This tool can calculate and display the number of bytes, lines, words, and characters in a specified file.

## Features

- **Byte Counts:** Calculate the total number of bytes in the file.
- **Line Counts:** Count the number of newline characters (`\n`) in the file.
- **Word Counts:** Count the number of words in the file.
- **Character Counts:** Count the total number of characters, including newlines.
- **All Counts:** When no specific option is provided, the tool outputs all counts at once (characters, words, lines, bytes).

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/OluwagbeminiyiA/ccwc.git
cd command-line-wc-tool
```

Ensure you have Python installed on your system.

## Usage

You can run the script from the command line:

```bash
python ccwc.py FILE [options]
```

### Positional Argument

- `FILE`: The path to the file you want to analyze.

### Options

- `-c, --bytes`: Print the byte counts of the file.
- `-l, --lines`: Print the newline counts of the file.
- `-w, --words`: Print the word counts of the file.
- `-m, --chars`: Print the character counts of the file.

### Examples

#### Calculate Byte Count

```bash
python ccwc.py example.txt --bytes
```

#### Calculate Line Count

```bash
python ccwc.py example.txt --lines
```

#### Calculate Word Count

```bash
python ccwc.py example.txt --words
```

#### Calculate Character Count

```bash
python ccwc.py example.txt --chars
```

#### Calculate All Counts

If you run the tool without any options, it will calculate and print all counts:

```bash
python ccwc.py example.txt
```

### Example Output

```bash
(256, 50, 15, 230)
```

Where:
- `256`: Character Count
- `50`: Word Count
- `15`: Line Count
- `230`: Byte Count

## Error Handling

If the specified file does not exist, the tool will print an error message:

```bash
Error: File 'filename.txt' not found.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

