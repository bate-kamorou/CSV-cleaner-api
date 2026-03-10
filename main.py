from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import FileResponse
from services import csv_cleaner
import pandas as pd
from pathlib import Path

#instantiate the fastapi app
app = FastAPI()

# Safe directory for storing cleaned CSVs
OUTPUT_DIR = Path("./cleaned_data")
OUTPUT_DIR.mkdir(exist_ok=True)

# health checker endpoint
@app.get("/health")
def health():
    return {
        "status": "Api running..."
    }, 400
# csv cleaner endpoint
@app.post("/clean-csv")
async def clean_csv(file: UploadFile = File(...), output_file_path: str = Query("cleaned_csv")):
    
    # Validate and sanitize output path to prevent path traversal attacks
    try:
        # Remove any directory separators and ".." to prevent traversal
        filename = Path(output_file_path).name
        if not filename or filename.startswith("."):
            return {
                "error": "Invalid filename. Filename cannot be empty or start with a dot."
            }, 400
        
        # Ensure the file has a .csv extension
        if not filename.endswith(".csv"):
            filename += ".csv"
        
        # Create the full path
        output_path = OUTPUT_DIR / filename
        
    except Exception as e:
        return {
            "error": f"Invalid output path: {str(e)}"
        }, 400

    df = pd.read_csv(file.file)

    cleaned_csv = csv_cleaner(df)

    # store the cleaned csv 
    cleaned_csv.to_csv(output_path, index=False)

    return {
        "message": "file successfully saved ✅",
        "rows": len(cleaned_csv),
        "saved_path": str(output_path)
    }

@app.get("/download")
def download_csv(path):
    file_path = OUTPUT_DIR / path
    if not file_path.exists():
        return {
            "error": "File not found."
        }, 404
    
    return FileResponse(str(file_path), media_type='text/csv', filename=file_path.name)


