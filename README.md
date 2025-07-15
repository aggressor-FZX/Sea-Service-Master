# Sea Service Master Application

A PySide6 (Qt for Python) desktop application designed to manage, analyze, and generate sea service letters from Excel data for maritime personnel.

## Overview

This application provides a graphical interface to:

- Load Excel files containing sea service records
- Display and manipulate calendar-based data tables of service days
- Calculate days underway, in port, leave, training, and other status categories
- Generate formatted sea service letters as Word documents, using customizable templates
- Support manual edits with instant recalculation and validation
- Copy table data easily for external use

It is built with **PySide6**, **pandas**, and integrates with Microsoft Word document generation (via a custom module).

## Features

- **Load and parse Excel files** of service data with configurable header row
- Interactive **calendar and letter tables** with color-coded day statuses (`U/W`, `I/P`, `L`, etc.)
- Automatic calculation of total days underway or in port
- Validation of date inputs and recalculation of day counts on-the-fly
- Customizable user inputs for personnel information (name, title, ship, ratings, etc.)
- Generates sea service letters in Word format using user-selected templates and output directories
- Copy selected table data to clipboard in tab-separated format for easy pasting
- Error handling and informative messages for invalid inputs

## Installation

Requires Python 3.x with the following dependencies:

- PySide6
- pandas
- openpyxl (for Excel reading)
- Your custom `Make_PDF` module for document generation

Install dependencies using:

```bash
pip install PySide6 pandas openpyxl
