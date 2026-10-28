from pathlib import Path

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
ALLOWED_EXTENSIONS = {".txt", ".pdf"}

def validate_upload(filename: str | None, data: bytes) -> str:
    extension = Path(filename).suffix.lower() if filename else None

    if extension not in ALLOWED_EXTENSIONS:
        raise ValueError("Only .txt and .pdf files are allowed")

    if not data:
        raise ValueError("The uploaded file is empty")

    if len(data) > MAX_FILE_SIZE:
        raise ValueError("File exceeds the 10 MB limit")

    if extension == ".txt":
        try:
            data.decode("utf-8")
        except UnicodeDecodeError:
            raise ValueError("Text files must be UTF-8 encoded")

    if extension == ".pdf" and not data.startswith(b"%PDF-"):
        raise ValueError("File does not appear to be a valid PDF")

    return extension
