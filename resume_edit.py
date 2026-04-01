import os
from pathlib import Path

from utils import PDFMetadataEditor

RESUMES = "/Users/mzhang/Documents/resumes"

RESUMES_folders = os.listdir(RESUMES)

for fol in RESUMES_folders:
    print(fol)
folder_choice = RESUMES_folders[int(input(f"which 1..{len(RESUMES_folders)}\n"))-1]

folder = os.path.join(RESUMES,folder_choice)

files = [p for p in Path(folder).rglob("*") if p.is_file()]
for f in files:
    editor = PDFMetadataEditor(str(f))
    editor.set_author("Michael Zhang")
    editor.set_creator("Michael Zhang")
    editor.set_keywords("")
    editor.set_producer("")
    editor.set_subject("")
    editor.set_title("MichaelJZhang-RESUME")
    f.rename(f.with_name("MichaelJZhang-RESUME.pdf"))