#!/usr/bin/env python3
"""
Convert CSV files to JSON for the China Climate Scorecard application.
This script converts both dataset-qual.csv and dataset-time-series.csv to JSON format.

Usage:
    python convert_csv_to_json.py

    OR (if executable):
    ./convert_csv_to_json.py

The script will look for CSV files in the same directory and create JSON files:
    - dataset-qual.csv → dataset-qual.json
    - dataset-time-series.csv → dataset-time-series.json
"""

import csv
import json
import sys
from pathlib import Path


def convert_csv_to_json(csv_file_path, json_file_path):
    """
    Convert a CSV file to JSON format.

    Args:
        csv_file_path: Path to input CSV file
        json_file_path: Path to output JSON file
    """
    try:
        # Read CSV file
        with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
            # Use DictReader to convert each row to a dictionary
            reader = csv.DictReader(csvfile)
            data = list(reader)

        # Write JSON file
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=2, ensure_ascii=False)

        print(f"✓ Successfully converted {csv_file_path} to {json_file_path}")
        print(f"  - Records converted: {len(data)}")
        if data:
            print(f"  - Fields: {', '.join(data[0].keys())}")

        return True

    except FileNotFoundError:
        print(f"✗ Error: File not found: {csv_file_path}", file=sys.stderr)
        return False
    except Exception as e:
        print(f"✗ Error converting {csv_file_path}: {str(e)}", file=sys.stderr)
        return False


def main():
    """Main function to convert both CSV files."""
    print("=" * 60)
    print("CSV to JSON Converter for China Climate Scorecard")
    print("=" * 60)
    print()

    # Get the script directory
    script_dir = Path(__file__).parent

    # Define file paths
    files_to_convert = [
        ('dataset-qual.csv', 'dataset-qual.json'),
        ('dataset-time-series.csv', 'dataset-time-series.json')
    ]

    success_count = 0

    for csv_file, json_file in files_to_convert:
        csv_path = script_dir / csv_file
        json_path = script_dir / json_file

        if convert_csv_to_json(csv_path, json_path):
            success_count += 1
        print()

    print("=" * 60)
    print(f"Conversion complete: {success_count}/{len(files_to_convert)} files converted successfully")
    print("=" * 60)

    return success_count == len(files_to_convert)


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
