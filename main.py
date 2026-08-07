from PIL import Image
from pathlib import Path
import pytesseract
import os
from docx import Document
from docx.shared import Inches

def get_input_path():
    dangerous_dir = [Path("C:/"),
    Path("C:/Users"),
    Path("C:/Windows"),
    Path("C:/Program Files"),
    Path(os.path.expanduser("~"))]
    c = input("Enter full path of the folder:")
    file_path = Path(c)

    if file_path.exists():
        print(f"The path '{file_path}' exists.")
    else:
        print(f"The path '{file_path}' does not exist.")
        exit()
    if file_path in dangerous_dir:
        print("Warning:System Directory Exiting.......")
        exit()
    return file_path

def write(path):
    document = Document()
    document.add_heading(path.name, 0)
    for a in path.rglob("*"):
        if a.suffix.lower() in [".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"]:
            try:
                p = pytesseract.image_to_string(Image.open(str(a)))
                document.add_paragraph(p)
            except Exception as e:
                print(f"Error processing {a}: {e}")
    document.save(path.stem+".docx")

c = get_input_path()
write(c)




