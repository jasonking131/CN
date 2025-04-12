import pytesseract
from PIL import Image
import os

# Explicit path configuration
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text(image_path):
    try:
        return pytesseract.image_to_string(
            Image.open(image_path),
            config='--psm 6 -l eng+chi_sim'
        )
    except Exception as e:
        print(f"OCR Error: {str(e)}")
        return ""
