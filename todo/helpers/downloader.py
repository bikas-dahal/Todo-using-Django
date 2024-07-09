import requests 
from pathlib import Path

def download_to_local(url, dest_path, parent_mkdir=True):
    if not isinstance(dest_path, Path):
        raise ValueError('path must be a Path object')
    
    if parent_mkdir:
        dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        dest_path.write_bytes(response.content) 
        return True
    except requests.RequestException as e:
        print(e)
        return False