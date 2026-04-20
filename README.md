# Log Analyzer (Python)

A simple log analysis tool built in Python that reads text-based log files and classifies messages based on severity levels.

## Features

* Counts occurrences of:

  * Errors
  * Warnings
  * Info messages
* Detects unmatched lines
* Displays results in console
* Optionally saves analysis to a report file with timestamp

## How it works

The script:

1. Reads a log file provided by the user
2. Processes it line by line
3. Classifies each line based on keywords
4. Displays a summary of results
5. Optionally generates a report file

## How to run

1. Make sure you have Python installed
2. Run the script:

```bash
python main.py
```

3. Enter the path to your log file when prompted

Example:

```bash
Enter log file path: test_log.txt
```

## Example output

```
Log Analysis Results:
Total lines analyzed: 6
Errors: 2
Warnings: 2
Info: 2
Unmatched lines: 0
```

## What I learned

* File handling in Python
* String processing and pattern detection
* Control flow (loops and conditionals)
* Error handling with try/except
* Basic automation and reporting

## Future improvements

* More precise log parsing (regex)
* Export results to CSV or JSON
* Support for large log files (streaming)
* Better classification system

## Author

Cristopher Delgado Tamariz
