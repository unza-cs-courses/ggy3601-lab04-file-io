# Your Assignment Parameters

These are your unique values for Lab 4. Use these exact values in your code.

## Dataset Parameters

| Parameter | Your Value |
|-----------|------------|
| Number of Records | {num_records} |
| Site Locations | {locations} |
| Depth Range | {depth_range} |
| Error Records | {include_errors} (records with data issues) |

Your personalized `data/samples.csv` file has been generated with these parameters.

---

## Task 1: Basic Text File I/O (20 marks)

Create `src/lab4_text_io.py` with functions to read and write text files.

```python
# lab4_text_io.py
"""
Lab 4 Task 1: Basic Text File I/O
Learn to read and write text files using context managers.
"""


def write_sample_log(filepath: str, samples: list) -> int:
    """
    Write sample information to a log file.

    Args:
        filepath: Path to the output file
        samples: List of sample dictionaries with 'id', 'rock_type', 'grade'

    Returns:
        Number of lines written

    Example:
        samples = [
            {'id': 'GEO-001', 'rock_type': 'Granite', 'grade': 2.5},
            {'id': 'GEO-002', 'rock_type': 'Basalt', 'grade': 1.8}
        ]
        count = write_sample_log('output.txt', samples)
    """
    # TODO: Implement this function
    # Use 'with' statement to open file for writing
    # Write header line: "Sample Log - Geological Survey"
    # Write separator line: "=" * 40
    # For each sample, write: "Sample {id}: {rock_type}, Grade: {grade}%"
    # Return total number of lines written
    pass


def read_sample_log(filepath: str) -> list:
    """
    Read sample information from a log file.

    Args:
        filepath: Path to the input file

    Returns:
        List of lines from the file (excluding header and separator)

    Example:
        lines = read_sample_log('output.txt')
        # Returns ['Sample GEO-001: Granite, Grade: 2.5%', ...]
    """
    # TODO: Implement this function
    # Use 'with' statement to open file for reading
    # Read all lines and skip header (first 2 lines)
    # Return list of sample lines (stripped of whitespace)
    pass


def append_to_log(filepath: str, message: str) -> None:
    """
    Append a message to an existing log file.

    Args:
        filepath: Path to the log file
        message: Message to append

    Returns:
        None
    """
    # TODO: Implement this function
    # Use 'with' statement to open file in append mode ('a')
    # Write message followed by newline
    pass


def count_lines(filepath: str) -> int:
    """
    Count the number of lines in a file.

    Args:
        filepath: Path to the file

    Returns:
        Number of lines in the file
    """
    # TODO: Implement this function
    # Use 'with' statement to open and read file
    # Count and return number of lines
    pass
```

---

## Task 2: Reading CSV Files (20 marks)

Create `src/lab4_csv_reader.py` with functions to read CSV data.

```python
# lab4_csv_reader.py
"""
Lab 4 Task 2: Reading CSV Files
Learn to read and parse CSV files using the csv module.
"""

import csv


def read_samples_as_list(filepath: str) -> list:
    """
    Read CSV file and return data as list of lists.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of lists (each inner list is a row, including header)

    Example:
        data = read_samples_as_list('data/samples.csv')
        header = data[0]  # ['sample_id', 'rock_type', ...]
        first_row = data[1]  # ['GEO-001', 'Granite', ...]
    """
    # TODO: Implement this function
    # Use csv.reader to read the CSV file
    # Return all rows as a list of lists
    pass


def read_samples_as_dict(filepath: str) -> list:
    """
    Read CSV file and return data as list of dictionaries.

    Args:
        filepath: Path to the CSV file

    Returns:
        List of dictionaries (each dict is a row with column names as keys)

    Example:
        samples = read_samples_as_dict('data/samples.csv')
        # [{'sample_id': 'GEO-001', 'rock_type': 'Granite', ...}, ...]
    """
    # TODO: Implement this function
    # Use csv.DictReader to read the CSV file
    # Return list of dictionaries
    pass


def get_column_values(filepath: str, column_name: str) -> list:
    """
    Extract all values from a specific column.

    Args:
        filepath: Path to the CSV file
        column_name: Name of the column to extract

    Returns:
        List of values from that column

    Example:
        grades = get_column_values('data/samples.csv', 'grade')
        # ['2.5', '1.8', '3.2', ...]
    """
    # TODO: Implement this function
    # Use csv.DictReader to read the file
    # Extract and return values from the specified column
    pass


def get_unique_values(filepath: str, column_name: str) -> set:
    """
    Get unique values from a specific column.

    Args:
        filepath: Path to the CSV file
        column_name: Name of the column

    Returns:
        Set of unique values from that column

    Example:
        rock_types = get_unique_values('data/samples.csv', 'rock_type')
        # {'Granite', 'Basalt', 'Sandstone'}
    """
    # TODO: Implement this function
    # Use get_column_values and convert to set
    pass
```

---

## Task 3: Writing CSV Files (20 marks)

Create `src/lab4_csv_writer.py` with functions to write CSV data.

```python
# lab4_csv_writer.py
"""
Lab 4 Task 3: Writing CSV Files
Learn to create and write CSV files using the csv module.
"""

import csv


def write_samples_from_list(filepath: str, header: list, rows: list) -> int:
    """
    Write data to a CSV file from lists.

    Args:
        filepath: Path to the output CSV file
        header: List of column names
        rows: List of lists (data rows)

    Returns:
        Number of data rows written (excluding header)

    Example:
        header = ['sample_id', 'rock_type', 'grade']
        rows = [
            ['GEO-001', 'Granite', '2.5'],
            ['GEO-002', 'Basalt', '1.8']
        ]
        count = write_samples_from_list('output.csv', header, rows)
    """
    # TODO: Implement this function
    # Use csv.writer to write header and rows
    # Return count of data rows written
    pass


def write_samples_from_dict(filepath: str, fieldnames: list, rows: list) -> int:
    """
    Write data to a CSV file from dictionaries.

    Args:
        filepath: Path to the output CSV file
        fieldnames: List of column names (determines order)
        rows: List of dictionaries (data rows)

    Returns:
        Number of data rows written

    Example:
        fieldnames = ['sample_id', 'rock_type', 'grade']
        rows = [
            {'sample_id': 'GEO-001', 'rock_type': 'Granite', 'grade': '2.5'},
            {'sample_id': 'GEO-002', 'rock_type': 'Basalt', 'grade': '1.8'}
        ]
        count = write_samples_from_dict('output.csv', fieldnames, rows)
    """
    # TODO: Implement this function
    # Use csv.DictWriter to write header and rows
    # Return count of data rows written
    pass


def filter_and_save(input_path: str, output_path: str,
                    column: str, min_value: float) -> int:
    """
    Read CSV, filter rows by numeric column, and save filtered data.

    Args:
        input_path: Path to input CSV file
        output_path: Path to output CSV file
        column: Name of the numeric column to filter
        min_value: Minimum value (inclusive) to include

    Returns:
        Number of rows in the filtered output

    Example:
        # Filter samples with grade >= 2.0
        count = filter_and_save('input.csv', 'output.csv', 'grade', 2.0)
    """
    # TODO: Implement this function
    # Read input CSV using DictReader
    # Filter rows where column value >= min_value
    # Write filtered rows to output CSV
    # Return count of filtered rows
    pass
```

---

## Task 4: Processing Geological CSV Data (25 marks)

Create `src/lab4_data_processor.py` with functions to analyze geological data.

```python
# lab4_data_processor.py
"""
Lab 4 Task 4: Processing Geological CSV Data
Apply file I/O skills to analyze geological sample data.
"""

import csv


def calculate_statistics(filepath: str, column: str) -> dict:
    """
    Calculate basic statistics for a numeric column.

    Args:
        filepath: Path to the CSV file
        column: Name of the numeric column

    Returns:
        Dictionary with 'count', 'sum', 'mean', 'min', 'max'

    Example:
        stats = calculate_statistics('data/samples.csv', 'grade')
        # {'count': 50, 'sum': 125.5, 'mean': 2.51, 'min': 0.5, 'max': 4.8}
    """
    # TODO: Implement this function
    # Read the CSV file and extract numeric values from the column
    # Calculate and return statistics
    # Handle conversion errors gracefully (skip invalid values)
    pass


def group_by_location(filepath: str) -> dict:
    """
    Group samples by their location.

    Args:
        filepath: Path to the CSV file

    Returns:
        Dictionary with location as key and list of sample_ids as value

    Example:
        groups = group_by_location('data/samples.csv')
        # {'Site-A': ['GEO-001', 'GEO-005', ...], 'Site-B': [...]}
    """
    # TODO: Implement this function
    # Read CSV and group samples by 'location' column
    # Return dictionary mapping location to list of sample_ids
    pass


def find_high_grade_samples(filepath: str, threshold: float) -> list:
    """
    Find samples with grade above the threshold.

    Args:
        filepath: Path to the CSV file
        threshold: Minimum grade value (exclusive)

    Returns:
        List of dictionaries for high-grade samples, sorted by grade (descending)

    Example:
        high_grade = find_high_grade_samples('data/samples.csv', 3.0)
        # [{'sample_id': 'GEO-023', 'grade': 4.5, ...}, ...]
    """
    # TODO: Implement this function
    # Read CSV and filter samples with grade > threshold
    # Sort by grade in descending order
    # Return list of sample dictionaries
    pass


def generate_summary_report(filepath: str, output_path: str) -> None:
    """
    Generate a text summary report of the sample data.

    Args:
        filepath: Path to the input CSV file
        output_path: Path to the output text file

    The report should include:
    - Total number of samples
    - Number of unique locations
    - Number of unique rock types
    - Grade statistics (min, max, mean)
    - Top 5 highest grade samples
    """
    # TODO: Implement this function
    # Read and analyze the CSV data
    # Write a formatted summary report to the output file
    pass
```

---

## Task 5: Error Handling (15 marks)

Create `src/lab4_error_handling.py` with robust file error handling.

```python
# lab4_error_handling.py
"""
Lab 4 Task 5: Error Handling for File Operations
Learn to handle file-related errors gracefully.
"""

import csv


def safe_read_file(filepath: str) -> tuple:
    """
    Safely read a file with proper error handling.

    Args:
        filepath: Path to the file to read

    Returns:
        Tuple of (success: bool, content_or_error: str)
        If successful: (True, file_content)
        If error: (False, error_message)

    Example:
        success, result = safe_read_file('missing.txt')
        if success:
            print(result)  # File content
        else:
            print(f"Error: {result}")  # Error message
    """
    # TODO: Implement this function
    # Use try/except to handle:
    # - FileNotFoundError: "File not found: {filepath}"
    # - PermissionError: "Permission denied: {filepath}"
    # - Exception: "Error reading file: {str(e)}"
    pass


def safe_read_csv(filepath: str) -> tuple:
    """
    Safely read a CSV file with error handling.

    Args:
        filepath: Path to the CSV file

    Returns:
        Tuple of (success: bool, data_or_error: list|str)
        If successful: (True, list_of_dicts)
        If error: (False, error_message)
    """
    # TODO: Implement this function
    # Handle file errors and CSV parsing errors
    pass


def safe_write_file(filepath: str, content: str) -> tuple:
    """
    Safely write to a file with error handling.

    Args:
        filepath: Path to write to
        content: Content to write

    Returns:
        Tuple of (success: bool, message: str)
        If successful: (True, "Successfully wrote to {filepath}")
        If error: (False, error_message)
    """
    # TODO: Implement this function
    # Handle PermissionError and other potential errors
    pass


def validate_csv_row(row: dict, required_fields: list,
                     numeric_fields: list = None) -> tuple:
    """
    Validate a CSV row has required fields and valid numeric values.

    Args:
        row: Dictionary representing a CSV row
        required_fields: List of field names that must be present
        numeric_fields: List of field names that must be numeric (optional)

    Returns:
        Tuple of (is_valid: bool, errors: list)

    Example:
        row = {'sample_id': 'GEO-001', 'grade': '2.5', 'depth': 'invalid'}
        valid, errors = validate_csv_row(
            row,
            required_fields=['sample_id', 'grade'],
            numeric_fields=['grade', 'depth']
        )
        # (False, ["Field 'depth' is not a valid number"])
    """
    # TODO: Implement this function
    # Check all required fields are present and non-empty
    # Check numeric fields can be converted to float
    # Return validation result and list of errors
    pass


def process_csv_with_validation(filepath: str) -> dict:
    """
    Process a CSV file, validating each row and reporting errors.

    Args:
        filepath: Path to the CSV file

    Returns:
        Dictionary with:
        - 'valid_rows': list of valid row dictionaries
        - 'invalid_rows': list of tuples (row_number, row, errors)
        - 'error_count': total number of invalid rows

    Example:
        result = process_csv_with_validation('data/samples.csv')
        print(f"Valid: {len(result['valid_rows'])}")
        print(f"Invalid: {result['error_count']}")
    """
    # TODO: Implement this function
    # Read CSV and validate each row
    # Collect valid and invalid rows
    # Return summary dictionary
    pass
```

---

## Testing Your Code

Run the automated tests locally:

```bash
# Run all visible tests
pytest tests/visible/ -v

# Run tests for a specific task
pytest tests/visible/test_lab4.py::TestTextIO -v
pytest tests/visible/test_lab4.py::TestCSVReader -v
pytest tests/visible/test_lab4.py::TestCSVWriter -v
pytest tests/visible/test_lab4.py::TestDataProcessor -v
pytest tests/visible/test_lab4.py::TestErrorHandling -v
```

## Tips

1. **Always use context managers** (`with` statement) - it ensures files are properly closed
2. **Handle encoding** - use `encoding='utf-8'` for cross-platform compatibility
3. **Validate data** - always check if values can be converted before processing
4. **Use newline=''** when opening CSV files to prevent blank line issues on Windows
5. **Test with edge cases** - empty files, missing columns, invalid data

## Code Quality Checklist

- [ ] All functions use context managers (`with` statement)
- [ ] Error handling covers common file errors
- [ ] CSV files opened with `newline=''`
- [ ] Comments explain the purpose of each function
- [ ] Variable names are descriptive

Push to GitHub to see your score on the Actions tab.
