# GGY3601 Lab 4: File I/O & CSV Processing

**Weight:** 15% of final grade
**Estimated Time:** 2-3 hours

## Purpose

This lab introduces file operations in Python, focusing on reading and writing text files and CSV data. You will learn to handle file-related errors gracefully and use context managers for safe file operations. These skills are essential for working with geological datasets stored in files.

## Learning Outcomes

By completing this lab, you will be able to:
- LO4.1: Read and write text files using Python's built-in functions
- LO4.2: Process CSV files using the csv module
- LO4.3: Handle file-related errors gracefully with try/except
- LO4.4: Use context managers (with statement) for file operations

## Your Personalized Assignment

**See `ASSIGNMENT.md` for your unique parameters and test values.**

The ASSIGNMENT.md file contains your student-specific values that you must use in your solutions. These values are unique to you and are used for automated testing.

## Repository Structure

```
.
├── src/
│   ├── lab4_text_io.py        # Task 1: Basic text file I/O
│   ├── lab4_csv_reader.py     # Task 2: Reading CSV files
│   ├── lab4_csv_writer.py     # Task 3: Writing CSV files
│   ├── lab4_data_processor.py # Task 4: Processing geological CSV data
│   └── lab4_error_handling.py # Task 5: Handling file errors
├── tests/
│   └── visible/               # Automated tests (visible to you)
├── data/
│   └── samples.csv            # Sample geological data
├── ASSIGNMENT.md              # Your unique assignment parameters
└── README.md                  # This file
```

## Key Concepts

### Context Managers (with statement)

Always use the `with` statement when working with files:

```python
# Correct: File automatically closed
with open('file.txt', 'r') as f:
    content = f.read()

# Avoid: Must remember to close
f = open('file.txt', 'r')
content = f.read()
f.close()  # Easy to forget!
```

### File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) |
| `'w'` | Write (overwrites existing) |
| `'a'` | Append (adds to end) |
| `'x'` | Exclusive create (fails if exists) |

### The csv Module

```python
import csv

# Reading CSV
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)  # row is a list

# Using DictReader
with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # row is a dictionary
```

### Error Handling

```python
try:
    with open('file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("Permission denied")
except Exception as e:
    print(f"An error occurred: {e}")
```

## Getting Started

1. Clone this repository to your local machine
2. Read `ASSIGNMENT.md` for your unique values
3. Explore the sample data in `data/samples.csv`
4. Complete each task in the `src/` directory
5. Run tests locally: `pytest tests/visible/ -v`
6. Push your code to see automated test results

## Testing Your Code

Run the automated tests locally:

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run tests for a specific file
pytest tests/visible/test_lab4.py::TestTextIO -v
```

## Submission

Push your completed code to this repository before the deadline. Your score is calculated from the automated tests.

## Academic Integrity

- **ALLOWED:** Lecture notes, official Python documentation, asking tutors
- **NOT ALLOWED:** Copying code, AI tools, sharing solutions

All submissions are checked with plagiarism detection software.
