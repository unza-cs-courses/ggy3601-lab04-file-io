"""
Lab 4 Visible Tests - File I/O & CSV Processing
"""

import subprocess
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent.parent.parent / "src"
DATA_DIR = Path(__file__).parent.parent.parent / "data"


def run_script(script_name, input_data=None):
    """Run a Python script and capture output."""
    script_path = SRC_DIR / script_name
    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        input=input_data,
        timeout=30
    )
    return result


class TestTask1TextIO:
    """Tests for basic text file I/O."""

    def test_text_io_file_exists(self):
        """lab4_text_io.py should exist."""
        assert (SRC_DIR / "lab4_text_io.py").exists()

    def test_text_io_runs(self):
        """lab4_text_io.py should run without errors."""
        result = run_script("lab4_text_io.py")
        assert result.returncode == 0, f"Error: {result.stderr}"


class TestTask2CSVReader:
    """Tests for CSV reading."""

    def test_csv_reader_exists(self):
        """lab4_csv_reader.py should exist."""
        assert (SRC_DIR / "lab4_csv_reader.py").exists()

    def test_csv_reader_runs(self):
        """lab4_csv_reader.py should run without errors."""
        result = run_script("lab4_csv_reader.py")
        assert result.returncode == 0, f"Error: {result.stderr}"


class TestTask3CSVWriter:
    """Tests for CSV writing."""

    def test_csv_writer_exists(self):
        """lab4_csv_writer.py should exist."""
        assert (SRC_DIR / "lab4_csv_writer.py").exists()


class TestTask4DataProcessor:
    """Tests for data processing."""

    def test_data_processor_exists(self):
        """lab4_data_processor.py should exist."""
        assert (SRC_DIR / "lab4_data_processor.py").exists()


class TestTask5ErrorHandling:
    """Tests for error handling."""

    def test_error_handling_exists(self):
        """lab4_error_handling.py should exist."""
        assert (SRC_DIR / "lab4_error_handling.py").exists()


class TestDataFiles:
    """Tests for data files."""

    def test_samples_csv_exists(self):
        """samples.csv should exist in data directory."""
        assert (DATA_DIR / "samples.csv").exists()
