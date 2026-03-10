
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
git clone https://github.com/bate-kamorou/CSV-cleaner-api.git
cd CSV_cleaner_api
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

- `POST /clean-csv` - Upload and clean  a CSV file
- `GET /download/<file_id>` - Download cleaned CSV

## Requirements

See `requirements.txt` for dependencies.
