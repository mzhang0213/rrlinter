import os
from pathlib import Path

from main import PDFMetadataEditor

RESUMES = "/Users/mzhang/Documents/resumes"

RESUMES_folders = os.listdir(RESUMES)

for fol in RESUMES_folders:
    print(fol)
folder_choice = RESUMES_folders[int(input(f"which 1..{len(RESUMES_folders)}\n"))-1]

folder = os.path.join(RESUMES,folder_choice)

files = [p for p in Path(folder).rglob("*") if p.is_file() and not p.name.startswith(".") and p.suffix == ".pdf"]

for f in files:
    new_folder = f.parent / f.stem
    new_folder.mkdir(exist_ok=True)
    new_file = new_folder / "MichaelJZhang-RESUME.pdf"

    editor = PDFMetadataEditor(str(f))
    editor.set_author("Michael Zhang")
    editor.set_creator("Michael Zhang")
    editor.set_keywords("")
    editor.set_producer("")
    editor.set_subject("")
    editor.set_title("MichaelJZhang-RESUME")
    editor.save(str(new_file))

    f.unlink()