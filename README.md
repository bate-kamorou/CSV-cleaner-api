
# CSV Cleaner API

A RESTful API for cleaning and processing CSV files.

## Features

- Upload and parse CSV files
- Data validation and cleaning
- Remove duplicates and handle missing values
- Export cleaned data
- RESTful endpoints for easy integration

## Installation

```bash
git clone <repository-url>
cd CSV_cleaner_api
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

- `POST /clean-csv` - Upload and clean  a CSV file
- `GET /clean/<file_id>` - Clean uploaded CSV
- `GET /download/<file_id>` - Download cleaned CSV

## Requirements

See `requirements.txt` for dependencies.
