# Spreadsheet Cleaner

A small Python tool that cleans messy CSV data: it removes duplicates and empty rows, standardizes names and dates, fixes number columns, and flags rows with missing or invalid amounts instead of silently hiding them.

## Before and after

**Before (messy_data.csv):** mixed-case names, extra spaces, duplicate rows, two date formats, text in a number column, blank rows.

**After (clean_data.csv):** consistent names, parsed dates, numeric amounts, 4 clean rows.

## How to run

pip install pandas
python cleaner.py

## What it does

- Removes duplicate and fully empty rows
- Strips extra spaces and fixes name capitalization
- Parses dates written in different formats
- Converts amounts to numbers
- Prints a warning listing any rows with missing or invalid amounts

## Notes

Dates like 01/12/2026 are read month-first (January 12). Confirm the date format with the data owner before using this on real data.

## Ideas for next steps

- Accept the file name as a command-line argument
- Export a summary (total per month, top customers)
