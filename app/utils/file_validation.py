ALLOWED_EXTENSIONS = {".csv", ".xlsx"}

def is_allowed_file(filename: str) -> bool:
    return any(filename.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS)
