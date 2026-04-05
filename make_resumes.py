import os
from dotenv import load_dotenv
from pathlib import Path

from rrlinter import PDFMetadataEditor

load_dotenv()

RESUMES = os.getenv("RESUME_PATH")

RESUMES_folders = os.listdir(RESUMES)

for fol in RESUMES_folders:
    print(fol)
folder_choice = RESUMES_folders[int(input(f"which 1..{len(RESUMES_folders)}\n"))-1]

folder = os.path.join(RESUMES,folder_choice)

files = [p for p in Path(folder).rglob("*") if p.is_file() and not p.name.startswith(".") and p.suffix == ".pdf"]

for f in files:
    if os.path.isdir(f):
        continue
    new_folder = f.parent / f.stem
    new_folder.mkdir(exist_ok=True)
    new_file = new_folder / (os.getenv("PDF_NAME") + (".pdf" if os.getenv("PDF_NAME")[:-4] != ".pdf" else ""))

    editor = PDFMetadataEditor(str(f))
    editor.set_author(os.getenv("MY_NAME"))
    editor.set_creator(os.getenv("MY_NAME"))
    editor.set_keywords("")
    editor.set_producer("")
    editor.set_subject("")
    editor.set_title(os.getenv("PDF_NAME"))
    editor.save(str(new_file))

    f.unlink()