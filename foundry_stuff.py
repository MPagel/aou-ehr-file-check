import os
from foundry.transforms import Dataset

def unzip_imported_zip(zipfile="input_resource"): 
    # Create a temporary file and ensure automatic cleanup using a context manager
    try:
        ds = Dataset.get(zipfile)
        ds_files = ds.files().download()
        return(ds_files)
    except Exception as e:
        print(f"An error occurred during unzip: {e}")

def extract_dl_location(file_dict):
    try:
        folder = os.path.dirname(list(file_dict.items())[0][1])
        return(folder)
    except Exception as e:
        print(f"An error occurred in location extractor: {e}")
